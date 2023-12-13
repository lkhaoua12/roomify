<div align="center">

# Roomify
</div>

### Cloning the repository

--> Clone the repository using the command below :
```bash
git clone https://github.com/lkhaoua12/roomify.git

```

--> Move into the directory where we have the project files : 
```bash
cd roomify

```

--> Create a virtual environment :
```bash
# Let's install virtualenv first
pip install virtualenv

# Then we create our virtual environment
virtualenv envname

```

--> Activate the virtual environment :
```bash
envname\bin\activate

```

--> Install the requirements :
```bash
pip install -r requirements.txt

```

#

### Running the App
--> First start a mysql docker-container :
```bash
docker run -d --name mysql-container \
    -e MYSQL_ROOT_PASSWORD=root \
    -e MYSQL_DATABASE=roomify \
    -e MYSQL_USER=root \
    -e MYSQL_PASSWORD=root \
    -p 3306:3306 \
    -v ~/roomify/mysql:/var/lib/mysql \
    mysql:latest \
    --character-set-server=utf8mb4 \
    --collation-server=utf8mb4_unicode_ci


--> To run the App, we use :
```bash
python manage.py runserver

```

> ⚠ Then, the development server will be started at http://127.0.0.1:8000/

#
### App preview
<table width="100%"> 
<tr>
<td width="50%">      
&nbsp; 
<br>
<p align="center">
  Feed Home
</p>
<img src="[https://imgur.com/a/JhN6hlm](https://i.imgur.com/BxxVOTf.png)https://i.imgur.com/BxxVOTf.png">
</table>

