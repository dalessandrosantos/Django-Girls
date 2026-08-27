from django.db import models
from django.conf import settings  # Importa as configurações do Django
from django.utils import timezone  # Importa recursos para trabalhar com data e hora

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # Se o usuário não estiver cadastrado no sistema, não poderá publicar.
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        """Publica o post e salva a data e hora da publicação."""
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title