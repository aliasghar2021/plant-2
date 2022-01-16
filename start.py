from button import buttonl
width   = 1200
height  = 880

w = 150
h = 80
x = int ( width / 2 - w / 2 )
y = 120

rects_w          = [ w , w , w , w ]
rects_h          = [ h , h , h , h ]
rects_x          = [ x , x , x , x ]
rects_y          = [ y , y * 2 + h , y * 3 + h * 2 , y * 4 + h * 3 ]
fps              = 100
color_list       = [ ( 0 , 255 , 0 ) , ( 0 , 255 , 0 ) , ( 0 , 255 , 0 ) , 
               ( 255 , 0 , 0 ) ]
click_color_list = [ ( 0 , 180 , 0 ) , ( 0 , 180 , 0 ) , ( 0 , 180 , 0 ) ,
                     ( 180 , 0 , 0 ) ]
txt_list         = [ 'PLAY' , 'SHOP' , 'SETTINGS' , 'QUIT' ]
txt_h_list       = [ 100    , 100    , 100        , 100    ]

but_1 = buttonl ( rects_x , rects_y , rects_w , rects_h , width ,
                         height , ( 255 , 255 , 255 ) , fps , 'Plant' , 
                         color_list , txt_list , txt_h_list , click_color_list )
but_1.button ()
