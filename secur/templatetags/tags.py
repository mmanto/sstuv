from django import template
from django.core.context_processors import request
from django.contrib.auth.models import User, Group

register = template.Library()



@register.inclusion_tag('menu.html')
def menu(user):
    

    print(user)
    print(user.groups.all())

      
    
    menu = []
    
    pase= { 'nombreDireccion' : 'Pases', 'target' : '/sig/pases/', 'subsistemas':   [       ]
           }
    
    expediente= { 'nombreDireccion' : 'Expedientes', 'target' : '/sig/expedientesLey/', 'subsistemas':  []         }
    
    mesaDeEntrada={ 'nombreDireccion' : 'Admin. Expedientes', 'subsistemas':
           
           [{ 'nombreSistema' : 'Expedientes', 'target' : '/sig/expedientes/'}, 
            {'nombreSistema' : 'Expedientes Ley',  'target' : '/sig/expedientesLey/'},
            {'nombreSistema' : 'Pases',  'target' : '/sig/pases/'},
            
           ]
           }
    
    regularizacion= { 'nombreDireccion' : 'Regularización', 'target' : '/sig/expedientes/', 'subsistemas':
           
           [{ 'nombreSistema' : 'Barrios', 'target' : ''}, 
            {'nombreSistema' : 'Encuadre Legal',  'target' : ''},
            {'nombreSistema' : 'Informe Urbanístico',  'target' : ''},
            {'nombreSistema' : 'Planos',  'target' : ''},
            {'nombreSistema' : 'Censo',  'target' : '/proc/regu/censo/nuevo/'},
            {'nombreSistema' : 'Doc. Adjudicación',  'target' : ''},
                     
           ]
           }
    
    
    familiaPropietaria= { 'nombreDireccion' : 'Familia Propietaria', 'subsistemas':
           
           [{ 'nombreSistema' : 'Tierras Afectadas', 'target' : ''}, 
            {'nombreSistema' : 'Informe Técnico Urbanístico',  'target' : ''},
            {'nombreSistema' : 'Planos', 'target' : ''},
            {'nombreSistema' : 'Censos', 'target' : ''},
            {'nombreSistema' : 'Doc. Adjudicación', 'target' : ''},
           ]
           }
    
    
    dir2= { 'nombreDireccion' : 'Ley 24374', 'subsistemas':
           
           [{ 'nombreSistema' : 'Inmuebles', 'target' : ''}, 
            { 'nombreSistema' : 'Regularización', 'target' : ''},
            { 'nombreSistema' : 'Consolidación', 'target' : ''},
            { 'nombreSistema' : 'Gestión Actas', 'target' : ''},
            
            ]
           }
   
    dir3= { 'nombreDireccion' : 'Escrituración', 'subsistemas':
           
           [
            { 'nombreSistema' : '', 'target' : ''}, 
           
           ]
           }
   
    dir4= { 'nombreDireccion' : 'Dirección Provincial de Escritura Social', 'subsistemas':
           
           [{ 'nombreSistema' : 'Pagos', 'target' : ''},
            { 'nombreSistema' : 'Registro Único Beneficiarios', 'target' : ''}, 
            
            ]
           }
    
    dir4= { 'nombreDireccion' : 'Urbanismo', 'subsistemas':
           
           [{ 'nombreSistema' : 'Municipios', 'target' : ''},
            { 'nombreSistema' : 'Planificación', 'target' : ''}, 
            { 'nombreSistema' : 'Informe Urbanístico DPIUT', 'target' : ''},
            { 'nombreSistema' : 'Pre-Factibilidad Urban&iacute;stica', 'target' : ''},
            { 'nombreSistema' : 'Ord. Territorial DL 8.912/77', 'target' : ''},
            ]
           }
    
    dir4= { 'nombreDireccion' : 'Mapa', 'subsistemas':
           
           [{ 'nombreSistema' : 'Barrios Regularización', 'target' : ''},
            { 'nombreSistema' : 'Encuadre Legal', 'target' : ''}, 
            { 'nombreSistema' : 'Tierra Familia Propietaria', 'target' : ''},
            { 'nombreSistema' : 'Informes urbanísticos', 'target' : ''},
            { 'nombreSistema' : 'Planos', 'target' : ''},
            { 'nombreSistema' : 'Conflictos Habitacionales', 'target' : ''},
            { 'nombreSistema' : 'Prosede', 'target' : ''},
            { 'nombreSistema' : 'inmuebles Ley 24374', 'target' : ''},
            ]
           }
    
    if( user.is_authenticated()):
            
          menu.append(expediente)
          menu.append(pase)  
#         menu.append(mesaDeEntrada)
          menu.append(regularizacion)
         
            
    
    
    
    return {'menu': menu, 'user': user}



def validateRol(user, rol):
    
    groups  = user.groups.all
    
    for group in groups:
        if(rol == group):
            return true
    return false    
 