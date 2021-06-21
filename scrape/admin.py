from django.contrib import admin
from .models import Amazon
from .models import Flipkart
from .models import Cowin
from .models import Help
from .models import Register

# Register your models here.

admin.site.register(Amazon)
admin.site.register(Flipkart)
admin.site.register(Cowin)
admin.site.register(Help)
admin.site.register(Register)