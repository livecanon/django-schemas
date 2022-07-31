# Querysets objects

- Określenie obiektu QuerySet nie powoduje żadnego działania w bazie danych. Działanie to następuje dopiero w momencie określenia zawartości obiektu.
- objects to domyślny menedżer każdego modelu, który pobiera wszystkie obiekty z bazy danych. [Istnieje możliwość zdefiniowania własnych menedżerów dla modelu](https://docs.djangoproject.com/en/4.0/topics/db/managers/). (book 42)

```
>> python manage.py shell
```

```
from django.contrib.auth.models import user
from blog.models import Post

user = User.objects.get(username='wasjakub')
```

## Creating objects

```

post = Post(
            title='Some title',
            slug='another-post',
            body='description',
            author=user
        )

post.save()
```

Alternatively, we can user _objects.create_ method:

```
Post.objects.create(
                title='Some title',
                slug='another-post',
                body='description',
                author=user
            )
```

## Updating objects

```
post.title = 'Updated title'
post.save()
```

## Getting all objects

```
all_posts = Post.objects.all()
```

## Filtering

```
filtered_values = Post.objects.filter(
                                publish__year=2022,
                                author__username='wasjakub'
                            )
```

## Excluding

NOTE: https://docs.djangoproject.com/en/4.0/ref/models/lookups/#

```
filtered_posts = Post.objects.filter(publish__year=2020) \
                    .exclude(title__startswith='Heheszki')
```

## Deleting object

```
post = Post.objects.delete(id=1)
post.delete()
```
