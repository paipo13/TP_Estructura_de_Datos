import csv
class App:
    def __init__(self,name,Category,Rating,Reviews,Size,Installs,Type,Price,Content_Rating,Genres,Last_Updated,Current_Ver,Android_Ver):
        self.name= name
        self.category = Category
        self.rating = Rating
        self.reviews = Reviews
        self.size = Size
        self.installs = Installs
        self.type = Type
        self.price = Price
        self.content_rating = Content_Rating
        self.genres = Genres
        self.last_updated = Last_Updated
        self.current_ver = Current_Ver
        self.android_ver = Android_Ver
    def __str__(self):
        return self.name

class Appstore:
    def __init__(self, name='Appstore', archivo_data='Play Store Data.csv'):
        self.name=name
        self.apps=set()
        self.apps_descargadas=set() 
        with open(archivo_data, mode='r', encoding='utf-8') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            for fila in lector_csv:
                object=App(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7],fila[8],fila[9],fila[10],fila[11],fila[12])
                self.apps.add(object)
    def descargar_app(self, name):
        app=None
        for object in self.apps:
            if object.name==name:
                app=object
        if app is None:
                print("No existe la app deseada.")      
        elif app not in self.apps_descargadas:
            self.apps_descargadas.add(app)
            print(f"Descargada la app {app.name}")
        else:
            print(f"La app {app.name} ya se encuentra descargada.")
            
    def eliminar_app(self, name):
        app=None
        for object in self.apps_descargadas:
            if object.name==name:
                app=object
        if app is None:
            print(f"La app {name} a eliminar no esta descargada.")
        else:
            self.apps_descargadas.remove(app)
            print(f"Eliminada la app {app.name}")