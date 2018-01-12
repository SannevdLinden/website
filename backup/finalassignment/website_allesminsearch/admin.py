from django.contrib import admin
from .models import Post
from .models import Depthdata
from .models import Bpdata
from .models import Frdata
from .models import Speeddata
from .models import Colorsetting

admin.site.register(Post)
admin.site.register(Depthdata)
admin.site.register(Bpdata)
admin.site.register(Frdata)
admin.site.register(Speeddata)
#admin.site.register(Colorsetting)
