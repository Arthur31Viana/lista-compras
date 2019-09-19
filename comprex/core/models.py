from django.db import models

class Categoria(models.Model):
    descricao = models.CharField('Descrição', max_length=50)

    class Meta:
        verbose_name_plural = 'Categorias'
        verbose_name = 'Categoria'

    def __str__(self):
        return self.descricao


class Produto(models.Model):
    descricao = models.CharField('Descrição', max_length=50)
    quantidade = models.IntegerField('Qnt.')
    preco = models.DecimalField('Preço', max_digits=10, decimal_places=3)
    categoria_id = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao

