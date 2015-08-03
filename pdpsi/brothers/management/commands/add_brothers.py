from django.core.management.base import BaseCommand, CommandError
from brothers.models import PClass, Brother

class Command(BaseCommand):

  def handle(self, *args, **options):
    class_names = ['Psi', 'Alpha Alpha', 'Alpha Beta', 'Alpha Gamma', 'Alpha Delta']

    for theclass in class_names:
      if (theclass == 'Psi'):
        Psi = PClass.objects.create(class_name=theclass, year_crossed='Spring 2012')
        Brother.objects.create(name='Alexander Park', pledge_class=Psi,
          pledge_name='Vash', line_number=83, active=True)
      if (theclass == 'Alpha Alpha'):
        Alpha_Alpha = PClass.objects.create(class_name=theclass, year_crossed='Spring 2013')
        Brother.objects.create(name='Victor Zhao', pledge_class=Alpha_Alpha,
          pledge_name='CRYSIS', line_number=88, active=True)
        Brother.objects.create(name='Richard C. Hsu', pledge_class=Alpha_Alpha,
          pledge_name='BALTO', line_number=90, active=True)
        Brother.objects.create(name='Jeffrey Lin', pledge_class=Alpha_Alpha,
          pledge_name='SQUID', line_number=91, active=True)
        Brother.objects.create(name='Brandon C. Eng', pledge_class=Alpha_Alpha,
          pledge_name='EXCALIBUR', line_number=92, active=True)
      if (theclass == 'Alpha Beta'):
        Alpha_Beta = PClass.objects.create(class_name=theclass, year_crossed='Fall 2013')
        Brother.objects.create(name='Brandon X. Yeh', pledge_class=Alpha_Beta,
          pledge_name='Hourglass', line_number=93, active=True)
        Brother.objects.create(name='Gray Guo', pledge_class=Alpha_Beta,
          pledge_name='PIP', line_number=96, active=True)
      if (theclass == 'Alpha Gamma'):
        Alpha_Gamma = PClass.objects.create(class_name=theclass, year_crossed='Fall 2014')
        Brother.objects.create(name='Jia Wen (Steven) Liu', pledge_class=Alpha_Gamma,
          pledge_name='Guy', line_number=97, active=True)
        Brother.objects.create(name='Taeyoon (Dan) Kim', pledge_class=Alpha_Gamma,
          pledge_name='ASCALON', line_number=98, active=True)
        Brother.objects.create(name='Brandon Yep', pledge_class=Alpha_Gamma,
          pledge_name='YES MAN', line_number=99, active=True)
        Brother.objects.create(name='Daniel Cho', pledge_class=Alpha_Gamma,
          pledge_name='Cal', line_number=100, active=True)
        Brother.objects.create(name='Michael Stewart', pledge_class=Alpha_Gamma,
          pledge_name='ICHIRO', line_number=101, active=True)
      if (theclass == 'Alpha Delta'):
        Alpha_Delta = PClass.objects.create(class_name=theclass, year_crossed='Spring 2015')
        Brother.objects.create(name='John Lee', pledge_class=Alpha_Delta,
          pledge_name='KEYBLADE', line_number=102, active=True)
        Brother.objects.create(name='Evan Mok', pledge_class=Alpha_Delta,
          pledge_name='Milgauss', line_number=103, active=True)
        Brother.objects.create(name='Alex Huang', pledge_class=Alpha_Delta,
          pledge_name='VERTIGO', line_number=104, active=True)
        Brother.objects.create(name='Jerry Pan', pledge_class=Alpha_Delta,
          pledge_name='RAY-BAN', line_number=105, active=True)
        Brother.objects.create(name='George Mao', pledge_class=Alpha_Delta,
          pledge_name='BASELINE', line_number=106, active=True)
        Brother.objects.create(name='Lawrence Hu', pledge_class=Alpha_Delta,
          pledge_name='SONOROUS', line_number=107, active=True)
        Brother.objects.create(name='Alex Ma', pledge_class=Alpha_Delta,
          pledge_name='Subversive', line_number=108, active=True)
        Brother.objects.create(name='Jason Zhou', pledge_class=Alpha_Delta,
          pledge_name='ASTRO', line_number=109, active=True)
        Brother.objects.create(name='Randy Tung', pledge_class=Alpha_Delta,
          pledge_name='BOSE', line_number=110, active=True)
      pass


