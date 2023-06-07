## index.html

```
<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <title>Tutorial Flask: Miniblog</title>
</head>

<body>
    {{ num_posts }} posts
</body>

</html>
```

## post_view.html

```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>{{ slug_title }}</title>
</head>

<body>
    Mostrando el post {{ slug_title }}
</body>

</html>
```

## post_form.html

```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>
        {% if post_id %}
        Modificando el post {{ post_id }}
        {% else %}
        Nuevo post
        {% endif %}
    </title>
</head>

<body>
    {% if post_id %}
    Modificando el post {{ post_id }}
    {% else %}
    Nuevo post
    {% endif %}
</body>

</html
```

## signup_form.html (con template parcial)

```
{% extends "base_template.html" %}
{% block title %}Registro de usuarios{% endblock %}
{% block content %}
    <form action="" method="post">
        <label for="name">Nombre: </label>
        <input type="text" id="name" name="name" /><br>
        <label for="email">Email: </label>
        <input type="text" id="email" name="email" /><br>
        <label for="password">Contraseña: </label>
        <input type="password" id="password" name="password" /><br>
        <input type="submit" id="send-signup" name="signup" value="Registrar" />
    </form>
{% endblock %}
```

**form.hidden_tag()**: acción para enviar código/token que evita ataques al form.
