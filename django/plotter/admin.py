from django.contrib import admin

from .models import Experiments
from .models import LimitDisplays
from .models import LimitOwnerships
from .models import Limits
from .models import MyUsers
from .models import PlotOwnerships
from .models import Plots
from .models import Users
    


# Register your models here.
admin.site.register(Experiments)
admin.site.register(LimitDisplays)
admin.site.register(LimitOwnerships)
admin.site.register(Limits)
admin.site.register(MyUsers)
admin.site.register(PlotOwnerships)
admin.site.register(Plots)
admin.site.register(Users)