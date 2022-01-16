import pygame
class button () :
    def __init__ ( self , x , y , w , h , dis_w , dis_h , dis_back , fps ,
                   caption , color , text , txt_h , click_color ) :
        self.x           = x
        self.y           = y
        self.w           = w
        self.h           = h
        self.dis_h       = dis_h
        self.dis_w       = dis_w
        self.dis_back    = dis_back
        self.fps         = fps
        self.color       = color
        self.text        = text
        self.txt_h       = txt_h
        self.click_color = click_color
        self.caption     = caption
    def button ( self ) :
        display = pygame.display.set_mode ( ( self.dis_w , self.dis_h ) )
        pygame.display.set_caption ( self.caption )
        clock = pygame.time.Clock ()
        def rect   () :
            mouse = pygame.mouse.get_pos ()
            m_x   = mouse [ 0 ]
            m_y   = mouse [ 1 ]
            if m_x in range ( self.x , self.x + self.w ) and m_y in range ( self.y
                              , self.y + self.h ) :
                pygame.draw.rect ( display , self.click_color , ( self.x , self.y , 
                               self.w , self.h ) )
            else :
                pygame.draw.rect ( display , self.color , ( self.x , self.y , 
                               self.w , self.h ) )
        def text ( msg , font ) :
            textSurface = font.render ( text , True , black )
            return textSurface , textSurface.get_rect ()
        while True :
            for event in pygame.event.get () :
                e_t = event.type
                if e_t == pygame.QUIT :
                    pygame.quit ()
                    quit ()
            display.fill ( self.dis_back )
            rect ()
            Text = pygame.font.Font ( 'freesansbold.ttf' , self.text_h )
            text ( self.text , Text )
            pygame.display.update ()
            clock.tick ( self.fps )
class buttonl () :
    def __init__ ( self , x , y , w , h , dis_w , dis_h , dis_back , fps ,
                   caption , color , text , txt_h , click_color ) :
        self.x           = x
        self.y           = y
        self.w           = w
        self.h           = h
        self.dis_h       = dis_h
        self.dis_w       = dis_w
        self.dis_back    = dis_back
        self.fps         = fps
        self.color       = color
        self.text        = text
        self.txt_h       = txt_h
        self.click_color = click_color
        self.caption     = caption
    def button ( self ) :
        display = pygame.display.set_mode ( ( self.dis_w , self.dis_h ) )
        pygame.display.set_caption ( self.caption )
        clock = pygame.time.Clock ()
        
        def rect   ( txt_h , msg , x , y , w , h , color , click_color ) :
            mouse = pygame.mouse.get_pos ()
            m_x   = mouse [ 0 ]
            m_y   = mouse [ 1 ]
            if m_x in range ( x , x + w ) and m_y in range ( y
                              , y + h ) :
                pygame.draw.rect ( display , click_color , ( x , y , 
                               w , h ) )
            else :
                pygame.draw.rect ( display , color , ( x , y , 
                               w , h ) )
            Text = pygame.font.Font ( 'freesansbold.ttf' , txt_h )
            text ( msg , Text )
        def text ( msg , font ) :
            textSurface = font.render ( text , True , black )
            return textSurface , textSurface.get_rect ()
        while True :
            for event in pygame.event.get () :
                e_t = event.type
                if e_t == pygame.QUIT :
                    pygame.quit ()
                    quit ()
            display.fill ( self.dis_back )
            for i in range ( 0 , len ( self.x ) ) :
                x           = self.x           [ i ]
                y           = self.y           [ i ]
                w           = self.w           [ i ]
                h           = self.h           [ i ]
                tx_h        = self.txt_h       [ i ]
                tt          = self.text        [ i ]
                color       = self.color       [ i ]
                click_color = self.click_color [ i ]
                rect ( tx_h , tt , x , y , w , h , color , click_color )
            pygame.display.update ()
            clock.tick ( self.fps )
