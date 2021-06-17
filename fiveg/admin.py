from django.contrib import admin
from .models import Person, Mentor, Auditor, Institution, Resume, \
    TraditionalQualification, CareerPath, FivegPortfolio, LearningGoal, \
    RealProjects, Deliverable


admin.site.register(Person)
admin.site.register(Mentor)
admin.site.register(Auditor)
admin.site.register(Institution)
admin.site.register(Resume)
admin.site.register(TraditionalQualification)
admin.site.register(CareerPath)
admin.site.register(FivegPortfolio)
admin.site.register(LearningGoal)
admin.site.register(RealProjects)
admin.site.register(Deliverable)

admin.site.site_header = "Glenboard Admin"
admin.site.site_title = "Glenboard Portal"
admin.site.index_title = "Welcome to Glenboard Portal"
