from django import template


register = template.Library()


@register.inclusion_tag('menu.html')
def menu():
    
    menu = []
    
    mesaDeEntrada={ 'nombreDireccion' : 'Mesa de Entrada', 'subsistemas':
           
           [{ 'nombreSistema' : 'Expedientes', 'target' : '/sig/expedientes/'}, 
            {'nombreSistema' : 'Expedientes Ley',  'target' : '/sig/expedientesLey/'},
            
           ]
           }
    
    
    dir1= { 'nombreDireccion' : 'Dirección Provincial de Infrastructura Urbana y Territorial', 'subsistemas':
           
           [{ 'nombreSistema' : 'Sub1', 'target' : ''}, 
            {'nombreSistema' : 'Sub2',  'target' : ''},
            {'nombreSistema' : 'Sub3', 'target' : ''},
           ]
           }
    
    
    dir2= { 'nombreDireccion' : 'Dirección Provincial de Coordinación de Programas Habitacionales', 'subsistemas':
           
           [{ 'nombreSistema' : 'Manejo saraza', 'target' : ''}, 
            
            ]
           }
   
    dir3= { 'nombreDireccion' : 'Dirección Provincial de Tierras', 'subsistemas':
           
           [
            { 'nombreSistema' : 'Manejo saraza', 'target' : ''}, 
           
           ]
           }
   
    dir4= { 'nombreDireccion' : 'Dirección Provincial de Escritura Social', 'subsistemas':
           
           [{ 'nombreSistema' : 'Manejo saraza', 'target' : ''}, 
            
            ]
           }
    
    menu.append(mesaDeEntrada)
#     menu.append(dir1)
#     menu.append(dir2)
#     menu.append(dir3)
#     menu.append(dir4)
    
    
    
    return {'menu': menu}
 