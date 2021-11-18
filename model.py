import tkinter as tk 

flower_List = [ "Rose" , "Lily" , "Lotus" , "Daisy" , "Jasmin" , "Sunflower" , "Marigold" , "Orchid" , "Blueble" , "Dahlia" ]

exist_Flower = [ "Rose" , "Sunflower" , "Daisy" , "Lotus" , "Marigold" ]

new = []

class Edit():
    pass #Ayda


class Add( tk.Frame ):
    def __init__( self , master , **kwargs ) :
        super( Add , self ).__init__(master)
        self.config ( bg = "#B0E0E6" , width = 600 , height = 400 )
        self.grid( row = 0 , column = 0 , padx= 200 , pady = 50 )
        self.fr_menu = tk.Frame( self , bd = 1 , relief = "solid" , padx = 100 , bg = "#c0c0c0" , width = 300 , height = 400  )
        self.fr_menu.grid ( row = 0 , column = 0 )
        self.lbl_menu = tk.Label( self.fr_menu , text = "Menu" , fg = "#483D8B" , bg = "#c0c0c0" )
        self.lbl_menu.grid ( row = 0 , column = 0  , sticky = "w" )
    
        i = 0 
        for flower in flower_List:
            
            if flower in exist_Flower:
                pass
            else :
                self.lbl_flower = tk.Label( self.fr_menu , text = flower , fg = "#483D8B" , bg = "#c0c0c0" )
                self.lbl_flower.grid( row = i , column = 0 , pady = 20 , sticky = "w" )
                new.append( flower )
            i = i + 1

        
        self.fr_lbl = tk.Frame( self , bd = 1 , relief = "solid" , padx = 100 , bg = "#DCDCDC" , width = 300 , height = 400  )
        self.fr_lbl.grid( row = 0 , column = 1 )





win = tk.Tk() 
win.geometry ("1000x800+300+50")
win.title( " Flower shopping " )
win.config( bg ="#FFEFD5")
flower1 = Add( win )
flower1.grid ( row = 1 , column = 1 )
win.mainloop()
