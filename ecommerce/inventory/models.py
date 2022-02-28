from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField

class Category(MPTTModel):
    """
    Category Table implimented with MPTT.
    """

    name = models.CharField(
        verbose_name=_("Category Name"),
        null=True,
        help_text=_("format: Required, max-100"),
        max_length=255,
        unique=False,
        blank=False,
    )
    slug = models.SlugField(
        max_length=200,
        verbose_name=_("Category safe URL"),
        unique=False,
        blank=False,
        null=False,
        help_text=_("format: required, letters, numbers, underscore, or hyphens")
    )
    parent = TreeForeignKey(
        "self",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="children",
    )
    is_active = models.BooleanField(default=True)  # Example Seasonal Lines

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name

        
