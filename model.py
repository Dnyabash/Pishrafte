import tkinter as tk 

flower_List = [ "Rose" , "Lily" , "Lotus" , "Daisy" , "Jasmin" , "Sunflower" , "Marigold" , "Orchid" , "Blueble" , "Dahlia" ]

exist_Flower = [ "Rose" , "Sunflower" , "Daisy" , "Lotus" , "Marigold" ]



class Edit():
    pass #Ayda


class Add( tk.Frame ):
    def __init__( self , master , **kwargs ) :
        super( Add , self ).__init__(master)
        self.grid( row = 0 , column = 0 , padx = 200  , pady = 100  )
        self.config ( bg = "#B0E0E6" )
        
        self.fr_menu = tk.Frame( self , bd = 1 , relief = "solid" , padx = 100 , bg = "#c0c0c0" )
        self.fr.grid ( row = 0 , column = 0 )
        self.lbl_meno = tk.Label( self.fr_menu , text = "Meno" , fg = "#483D8B" , bg = "#c0c0c0" )
        self.lbl_meno.grid ( row = 0 , column = 0  , sticky = "w" )










win = tk.Tk() 
win.geometry ("1000x800+300+150")
win.title( " Flower shopping " )
win.config( bg ="#FFEFD5")
flower1 = Add( win )
flower1.grid ( row = 1 , column = 1 )
win.mainloop()
