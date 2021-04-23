import time
import os

clear = lambda :os.system('cls')

def run():
    showintro()
#UI
def showintro():
    showtitle()
    #time.sleep(3)
    showmenu()
def showtitle():
    clear()
    print("""
    
    ██████╗ ██████╗  ██████╗ ██╗    ██╗███╗   ██╗███████╗██████╗     ██╗███╗   ██╗     █████╗ ██╗      ██████╗ ██████╗ ██╗  ██╗ ██████╗ ██╗     
    ██╔══██╗██╔══██╗██╔═══██╗██║    ██║████╗  ██║██╔════╝██╔══██╗    ██║████╗  ██║    ██╔══██╗██║     ██╔════╝██╔═══██╗██║  ██║██╔═══██╗██║     
    ██║  ██║██████╔╝██║   ██║██║ █╗ ██║██╔██╗ ██║█████╗  ██║  ██║    ██║██╔██╗ ██║    ███████║██║     ██║     ██║   ██║███████║██║   ██║██║     
    ██║  ██║██╔══██╗██║   ██║██║███╗██║██║╚██╗██║██╔══╝  ██║  ██║    ██║██║╚██╗██║    ██╔══██║██║     ██║     ██║   ██║██╔══██║██║   ██║██║     
    ██████╔╝██║  ██║╚██████╔╝╚███╔███╔╝██║ ╚████║███████╗██████╔╝    ██║██║ ╚████║    ██║  ██║███████╗╚██████╗╚██████╔╝██║  ██║╚██████╔╝███████╗
    ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝╚══════╝╚═════╝     ╚═╝╚═╝  ╚═══╝    ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝

                                          _     _    _   _             _    _  _      _ 
                                         / //|//_`  / | /_///|//_///|// `  / `/_//|,//_`
                                        /_// |/_,  /_.'/ \// |/`\// |/_;  /_;/ //  //_, 
                
                ....              .,***,(//(  ,**,   ,(#%&&&%(,   ,*//*,.  ((((*,,,....   ,,/(/* (%&&&%#(*.#%%%**.  
                .,,.  .              ....,*,,*,,,.. ,(#%&&&&&%#(,..,***.. ./(#,,,*/,,.   .,,/**,.*(##((/*,,.......  
                ..,. ,*,          . .,,...*/((/((((/(#%%%&&&%&%#/,*/((/*,,.**//,/%#%(** ((((,.. .,(%&&&%#(*.,(##(/**
                  .. ,**.  ... ., . .,..../((#(###(((##%%%%%%%#/*,*///*/((/....,/###*.(((/,,,,. ./#%&&%###(*/#%%%%#(
                 .,,.      ...,,,,...,....*((#(####((#%%%%##%##(*,*/((/(##(,..,*(###,,(((..,,,. ./#%%%%##(///%%&%%#(
                ,/(#/*     ,*//,, . ......*/(#(##((((##%&&&&&##(*,,***,*//&&&&&%%&&&&&&@@@@@&//,,(%&&&%%#(/*/#%&%##(
                /(%%%#*,. .,/(/*,. ..,,...*/(#(#&&&@@@&&&&&&&&&@&&&#*,.%&&&&&&&&&&&&&&&&@@@@&&&*(%&&&&&%%(///#%&%%#(
                **(##(*,. ./(((*.   .,,,, ,**/%&&&&&&&&&&&&&&&&&&&&&*/%&&&&&&&&&&&&&&&&&@@@@&&&/#%##(##((/,*/#%&%##(
                  ,*,. ... ,/(/*,.  .,*,,.,...&&&&&&&&&&&%%%&&&&&%%##,%%&&&&&&&%%%&&&&&&&@@@@@&&#####,((/**//(###((/
                  ,*,. ..  .,**. . .***,,.., /&&&&&&&%%%%%%%%&&&%%##*.#%%%%%%%%%%%%%%%&&&&@@@@@%*((#*%%%/,.,,,.,,.. 
                  ...            ,(/,#(/*,*/#%&&&&&&%%%%%%%%%%%%%##(..###%%%%%####%%%%&&&&&&&&&& ....(#&#. ....,....
                                 (((        #%&&&&%%%%%%%%%%%%%%##((**(//*/******,******(/(##%#%      %(@%.,**,     
                ((/.           .&(/.    ..***%%%%%%%%######%###%(((%/((,,**(//,,*.*,/,,/(**///((/ ..,,/&/%,,##(,    
                %%#* /##%/*.  .*#/#,.  .,(%%((%((/*/**,,(*,*/,**#(/%,((,**,/#*,*,,/,/,,*,/*/(/*/#,*###(&&&#,///.    
                ###* *###((*  ,#/#/,.  .*(%%//#(/***/*,/*..,****(//(  .*/*./(**,,*/,#*,*,(/*///*#,/%%%#%@#%/(/*.   .
                ((*. */(((/,  ,&*#,,    ./##((#*/*/,*,,(*,.,.,**/,/*. .,(*,(/*/,***,****,(/*((/,#//###(%&(&***,,   /
                *,,. .,///*.   #%(*       .((%(/*/,*/,*/*,,,,,/,%*(.,,,*(*,/#(/**,**,,**,(//((/*#(/*//*#%#@,,,,*// *
                ,      .,,.   . (/#(,,.,*//(/#**/,,**,//*,***,/,*/(((((#***/&#/(*(*,(,,*,*///(///%***(##&#&***,##(&&
                . *,*,...,. ,.,,..,/*##(,(#(#/*/..,.,,/(,,,,,,/.(//(##(/***/%(/(//*,(*,,,*/(*(//*&,*##%&&%//(****#@@
                ,*((/*,,*,*,.,,,***,.,**#%(/#//*,.,..,,..,..,,*,/*#**//*/*/*/*****,,*,.,*,*/*/(/,#(%#%/(,/((((/*,(#%
                (%%##,*/((/***///***,,,**,%%#*****..*.,,..,****//(((##(/(/,*,***,.,......,**,//(*##(,, .*/(((/**,,//
                ((/*,,*/((/*****,***,..,*###/##(((/,*,,, .,,,/**/(#(###/#((/(/,**,,,/,,,,,,**(##%/#/**..*//(((/*,.,*
                //*,,,*/((/*,,,**/**...,%#((%#(//////(/(/(*(/####%%/##(*#%%#(#(//(//(//((((####%%##&*, .,*/(((/*,...
                //*, ,,*/**,  .,,,,.   .,*((%#(((*/**//*(/*/((/((/#.....#(((((##//((/**/(((///((#%###(/...,*/*,..,/(
                #((,.*/((/*,  .,,,,.   .,*///*,.,**//////((((((///,..***,*/(((/((//////*////*******(((/...,,**,..,**
                ((/.  .*...    ......  .,***((***//****,**/**(*///(,*//*(////(%&#/(****,**//****%(////*,....//*,,,,*
                .,..             .      /(/(#(/,,*,,,,,.....,/*//#(,,***//**//#(/****,*****,,**###((,,,,,,,,**,,.,,,
                    `....     `...     `..`........                                       

                                                        ABSTRACT STUDIOS 2021

                                 ******************PRESIONA ENTER PARA CONTINUAR******************

    """)
    input()
def showerror():
    print("Ingresa un numero valido")
    time.sleep(2)
    showmenu()
def showinstructions():
    clear()
    print("""
        s.  .s    s.  .s5SSSs.  .s5SSSSs. .s5SSSs.  .s    s.  .s5SSSs.  .s5SSSs.  s.  .s5SSSs.  .s    s.  .s5SSSs.  .s5SSSs.  
        SS.       SS.       SS.    SSS          SS.       SS.       SS.       SS. SS.       SS.       SS.       SS.       SS. 
        S%S sSs.  S%S sS    `:;    S%S    sS    S%S sS    S%S sS    `:; sS    `:; S%S sS    S%S sSs.  S%S sS    `:; sS    `:; 
        S%S SS`S. S%S SS           S%S    SS    S%S SS    S%S SS        SS        S%S SS    S%S SS`S. S%S SS        SS        
        S%S SS `S.S%S `:;;;;.      S%S    SS .sS;:' SS    S%S SS        SS        S%S SS    S%S SS `S.S%S SSSs.     `:;;;;.   
        S%S SS  `sS%S       ;;.    S%S    SS    ;,  SS    S%S SS        SS        S%S SS    S%S SS  `sS%S SS              ;;. 
        `:; SS    `:;       `:;    `:;    SS    `:; SS    `:; SS        SS        `:; SS    `:; SS    `:; SS              `:; 
        ;,. SS    ;,. .,;   ;,.    ;,.    SS    ;,. SS    ;,. SS    ;,. SS    ;,. ;,. SS    ;,. SS    ;,. SS    ;,. .,;   ;,. 
        ;:' :;    ;:' `:;;;;;:'    ;:'    `:    ;:' `:;;;;;:' `:;;;;;:' `:;;;;;:' ;:' `:;;;;;:' :;    ;:' `:;;;;;:' `:;;;;;:' 

        ======================================================================================================================

                                    TIME TO  GET Riggity Riggity Wrecked Son!

        1 - Rellena tu bebida.
        2 - Cerveza y bebidas preparadas son una categoria. Shots son otra categoria de bebida.
        3 - Un jugador sera designado para ser el anfitrion o manager del juego. Este jugador tambien bebe.
        4 - Las reglas del juego son las mismas que el juego del ahorcado: Se tiene que adivinar la palabra en la pantalla
        5 - Tienes que esperar tu turno para dar una letra para adivinar la palabra. Los turnos son asignados al azar.
        6 - Si no adivinas una letra en la palabra, bebes un sorbo de tu bebida. Un sorbo equivale a 1/3 de shot.
        7 - La persona que adivine la palabra completa puede elegir otro jugador para participar en un SHOT_VERDAD_RETO
        8 - El reto y la verdad son puestos por la misma persona ganadora.
        9 - El ganador es registrado por el manager del juego.
        9 - Una "ronda" es cuando todos los jugadores han dado una vuelta en su participacion.
        10 - Al final de cada "ronda" todos los jugadores dan un shot. Si no tienes shot, puedes beber 3 sorbos de tu bebida.
        11 - El juego termina en la palabra 15.
        12 - Al final del juego, todos terminan su bebida... como la tengan.
        13 - El jugador que mas palabras adivino es premiado al final del juego.

   
   
          *************BEBER CON RESPONSABILIDAD ES LA ACTIVIDAD MAS DIVERTIDA DE TODAS. SI TOMAS, NO MANEJES.*************

    """)
    input("Presiona enter para continuar: ")
    showmenu()
def showus():
    clear()
    print("""
         .S_SSSs     .S_SSSs      sSSs  sdSS_SSSSSSbs   .S_sSSs     .S_SSSs      sSSs  sdSS_SSSSSSbs          sSSs  sdSS_SSSSSSbs   .S       S.    .S_sSSs     .S    sSSs_sSSs      sSSs         .S_SsS_S.    .S S.   
        .SS~SSSSS   .SS~SSSSS    d%%SP  YSSS~S%SSSSSP  .SS~YS%%b   .SS~SSSSS    d%%SP  YSSS~S%SSSSSP         d%%SP  YSSS~S%SSSSSP  .SS       SS.  .SS~YS%%b   .SS   d%%SP~YS%%b    d%%SP        .SS~S*S~SS.  .SS SS.  
        S%S   SSSS  S%S   SSSS  d%S'         S%S       S%S   `S%b  S%S   SSSS  d%S'         S%S             d%S'         S%S       S%S       S%S  S%S   `S%b  S%S  d%S'     `S%b  d%S'          S%S `Y' S%S  S%S S%S  
        S%S    S%S  S%S    S%S  S%|          S%S       S%S    S%S  S%S    S%S  S%S          S%S             S%|          S%S       S%S       S%S  S%S    S%S  S%S  S%S       S%S  S%|           S%S     S%S  S%S S%S  
        S%S SSSS%S  S%S SSSS%P  S&S          S&S       S%S    d*S  S%S SSSS%S  S&S          S&S             S&S          S&S       S&S       S&S  S%S    S&S  S&S  S&S       S&S  S&S           S%S     S%S  S%S S%S  
        S&S  SSS%S  S&S  SSSY   Y&Ss         S&S       S&S   .S*S  S&S  SSS%S  S&S          S&S             Y&Ss         S&S       S&S       S&S  S&S    S&S  S&S  S&S       S&S  Y&Ss          S&S     S&S   SS SS   
        S&S    S&S  S&S    S&S  `S&&S        S&S       S&S_sdSSS   S&S    S&S  S&S          S&S             `S&&S        S&S       S&S       S&S  S&S    S&S  S&S  S&S       S&S  `S&&S         S&S     S&S    S_S    
        S&S    S&S  S&S    S&S    `S*S       S&S       S&S~YSY%b   S&S    S&S  S&S          S&S               `S*S       S&S       S&S       S&S  S&S    S&S  S&S  S&S       S&S    `S*S        S&S     S&S   SS~SS   
        S*S    S&S  S*S    S&S     l*S       S*S       S*S   `S%b  S*S    S&S  S*b          S*S                l*S       S*S       S*b       d*S  S*S    d*S  S*S  S*b       d*S     l*S        S*S     S*S  S*S S*S  
        S*S    S*S  S*S    S*S    .S*P       S*S       S*S    S%S  S*S    S*S  S*S.         S*S               .S*P       S*S       S*S.     .S*S  S*S   .S*S  S*S  S*S.     .S*S    .S*P        S*S     S*S  S*S S*S  
        S*S    S*S  S*S SSSSP   sSS*S        S*S       S*S    S&S  S*S    S*S   SSSbs       S*S             sSS*S        S*S        SSSbs_sdSSS   S*S_sdSSS   S*S   SSSbs_sdSSS   sSS*S         S*S     S*S  S*S S*S  
        SSS    S*S  S*S  SSY    YSS'         S*S       S*S    SSS  SSS    S*S    YSSP       S*S             YSS'         S*S         YSSP~YSSY    SSS~YSSY    S*S    YSSP~YSSY    YSS'          SSS     S*S  S*S S*S  
               SP   SP                       SP        SP                 SP                SP                           SP                                   SP                                        SP   SP       
               Y    Y                        Y         Y                  Y                 Y                            Y                                    Y                                         Y    Y        
                                                                                                                                                                                                              
                ░                                      ░                                                ░                                                   
    """)
    print("Abstract Studios MX.")
    print("Todos los derechos no reservados.")
    print("Si tienes una idea increible para mejorar este juego, agregalo a la branch y solicita la publicacion")
    print("Sera un gusto tener un juego cada vez mas divertido y probado por la comunidad")
    print("Visita Nuestra Web> abstractstudios.com.mx")


    input("Presiona enter para continuar: ")
    showmenu()
def showmenu():
    clear()
    print("""
             ██╗██╗                            ██╗██╗   ██╗ ██████╗  █████╗ ██████╗                            
            ███║╚██╗                           ██║██║   ██║██╔════╝ ██╔══██╗██╔══██╗                           
            ╚██║ ██║                           ██║██║   ██║██║  ███╗███████║██████╔╝                           
             ██║ ██║                      ██   ██║██║   ██║██║   ██║██╔══██║██╔══██╗                           
             ██║██╔╝                      ╚█████╔╝╚██████╔╝╚██████╔╝██║  ██║██║  ██║                           
             ╚═╝╚═╝                        ╚════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝                           
                                                                                                                             
            ██████╗ ██╗ ██╗███╗   ██╗███████╗████████╗██████╗ ██╗   ██╗ ██████╗ ██████╗██╗ ██████╗ ███╗   ██╗███████╗███████╗
            ╚════██╗╚██╗██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║   ██║██╔════╝██╔════╝██║██╔═══██╗████╗  ██║██╔════╝██╔════╝
             █████╔╝ ██║██║██╔██╗ ██║███████╗   ██║   ██████╔╝██║   ██║██║     ██║     ██║██║   ██║██╔██╗ ██║█████╗  ███████╗
            ██╔═══╝  ██║██║██║╚██╗██║╚════██║   ██║   ██╔══██╗██║   ██║██║     ██║     ██║██║   ██║██║╚██╗██║██╔══╝  ╚════██║
            ███████╗██╔╝██║██║ ╚████║███████║   ██║   ██║  ██║╚██████╔╝╚██████╗╚██████╗██║╚██████╔╝██║ ╚████║███████╗███████║
            ╚══════╝╚═╝ ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚══════╝
                                                                                                                             
            ██████╗ ██╗         ███╗   ██╗ ██████╗ ███████╗ ██████╗ ████████╗██████╗  ██████╗ ███████╗       
            ╚════██╗╚██╗        ████╗  ██║██╔═══██╗██╔════╝██╔═══██╗╚══██╔══╝██╔══██╗██╔═══██╗██╔════╝       
             █████╔╝ ██║        ██╔██╗ ██║██║   ██║███████╗██║   ██║   ██║   ██████╔╝██║   ██║███████╗       
             ╚═══██╗ ██║        ██║╚██╗██║██║   ██║╚════██║██║   ██║   ██║   ██╔══██╗██║   ██║╚════██║       
            ██████╔╝██╔╝        ██║ ╚████║╚██████╔╝███████║╚██████╔╝   ██║   ██║  ██║╚██████╔╝███████║       
            ╚═════╝ ╚═╝         ╚═╝  ╚═══╝ ╚═════╝ ╚══════╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝                                                                                                                     
    """)
    menu_option = input("Opcion: ")
    assert menu_option.isnumeric(), showerror()
    
    menumanager(menu_option)


#GAME
def startgame():
    clear()
    

#MANAGERS
def menumanager(menu_option):
    menu_option = int(menu_option)
    assert menu_option>=1 and menu_option<4, showerror()
    if menu_option == 1:
        startgame()
    elif menu_option == 2:
        showinstructions()
    elif menu_option == 3:
        showus()
    else:
        print("Error Inexplicable")
        showmenu()  
def wordpicker():
    


if __name__ == "__main__":
    run()
    