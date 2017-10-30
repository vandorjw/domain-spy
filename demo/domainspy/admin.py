from django.contrib import admin
from .models import Domain
from .models import DomainURI
from .models import DomainRank
from .models import Technology
from .models import DomainTechnology

admin.site.register(Domain)
admin.site.register(DomainURI)
admin.site.register(DomainRank)
admin.site.register(Technology)
admin.site.register(DomainTechnology)
