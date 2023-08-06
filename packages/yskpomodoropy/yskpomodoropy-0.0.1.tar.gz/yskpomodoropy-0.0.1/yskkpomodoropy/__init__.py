import os
import time
def plus():
    
    a = open("yskpomodoropy.yskpomodoro","a")
    a.write("""+""")
    


class pomodoro:
    muzik1 = ""
    muzik2 = ""
    muzik3 = ""
    video = ""
    derssure = 0
    tenefussure = 0
    baslik = ""
    pp = ""
    def elmas(self):
        e = open("yskpomodoropy.yskpomodoro","r")
        elmas = str(len(e.read())+1)
        kode = """<head>
    <style>
        body{
            background-color: black;
            
        
        }
        p{
            text-shadow: 0.2px 0.2px 0.2px ;
            text-align: center;
            font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
            scrollbar-shadow-color: gold;
            color: blue;
            font-size: 500%;
        }
    </style>
</head>

<body onload="draw();">
    <div id="u">
        <canvas id="canvas" width="1000" height="250"></canvas>

    </div>
    <p>"""+elmas+""" Elmasa sahipsiniz</p>
    
    <script>
        function draw() {
  var canvas = document.getElementById('canvas');
  if (canvas.getContext){
    var ctx = canvas.getContext('2d');
    var x=650; var y=100;
    var w=200; var h=200;
    colors=['#3366CC','#003399','#333399'];
    sketch(x,y,w,h,ctx,colors);
  }
}

 function sketch(x,y,w,h,ctx,colors){
    ctx.fillStyle=colors[0];
    ctx.beginPath();
    ctx.moveTo(x,y);
    ctx.lineTo(x+w/2,y+0.7*h);
    ctx.lineTo(x+w/2,y);
    ctx.fill();
    
    ctx.fillStyle=colors[1];
    ctx.beginPath();
    ctx.moveTo(x+w/2, y);
    ctx.lineTo(x+w/2,y+0.7*h);
    ctx.lineTo(x+w,y);
    ctx.fill();
    
    
    ctx.beginPath();
    ctx.moveTo(x+w/4,y-0.3*h);
    ctx.lineTo(x,y);
    ctx.lineTo(x+w/2,y);
    ctx.fill();
    
    
    ctx.fillStyle=colors[2];
    ctx.beginPath();
    ctx.moveTo(x+w/4,y-0.3*h);
    ctx.lineTo(x+w/2,y);
    ctx.lineTo(x+0.75*w,y-0.3*h);
    ctx.fill();
    
   
    ctx.fillStyle=colors[0];
    ctx.beginPath();
    ctx.moveTo(x+0.75*w,y-0.3*h);
    ctx.lineTo(x+w/2,y);
    ctx.lineTo(x+w,y);
    ctx.fill();

 }
 draw()
 sketch()

</script>
</body>
"""
        s = open("elmaslar.html","w")
        s.write(kode)
        os.startfile("elmaslar.html")
        
    def basla(self):
        ss = time.time()
        derssure = str(self.derssure)
        tenefussure = str(self.tenefussure)
        
        if(len(self.pp)>2)and(len(self.baslik)):
            kod = """<!DOCTYPE html>
<html lang="tr">
<head>

    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>"""+self.baslik+"</title"+""">
    <link rel="icon" type="image/x-icon" href='"""+self.pp+"'"

        
        elif(len(self.baslik)>2):
            kod = """<!DOCTYPE html>
<html lang="tr">
<head>

    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>"""+self.baslik+"</title"  
        
        elif(len(self.pp)>2):
             kod = """!DOCTYPE html>
<html lang="tr">
<head>

    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" type="image/x-icon" href='"""+self.pp+"'"

        else:
            kod = """<!DOCTYPE html>
<html lang="tr">
<head>

    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content='width=device-width, initial-scale=1.0'"""

        if(len(self.video)>2):
            kod = kod + """>
    <style>
        html{
            height: 100%;
        }
        button{
            padding: 7px 7px;
            font-size: 10px;
            color: aquamarine;
            background-color: black;
            font-family: 'Times New Roman', Times, serif;
            transition: 1s;
            opacity: 0.7; 
            
        }
        button:hover{
            font-size: 13px;
            color: green;
            background-color: aquamarine;
            scrollbar-shadow-color: aquamarine;
            box-shadow: 0.5px 0.5px 0.5px 0.5px,1px 1px 1px 1px,1.5px 1.5px 1.5px 1.5px;
            opacity: 1;
            font-style: bold;
        }
        
        body{
            height: 100%;
            background-color: aquamarine;
        }
        .a{
            height: 25%;
            text-align: left;
        }

        audio{
            
            color: rgb(52, 79, 81);
            size: 100%;
            height: 15%;
            font-size: 2%;
            font-style: italic;
        }
        #sayac{
            color: black;
            size: 5%;
            height: 5%;
            font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
            font-weight: bold;
            text-align: left;
            text-shadow: 1px 1px 5px rgb(57, 71, 82);
        }
        .aktif{
            text-shadow:1px 1px 15px rgb(255, 160, 160);
            color:rgb(255, 0, 0);
            text-align: left;
            font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
            font-size:150%;
            font-weight: bold;
        }
        .pasif{
            opacity: 0.7;
            color: rgb(191, 220, 246);
            text-align: left;
            font-size: 75%;
            font-weight: lighter;
        }
        #y{
            text-align: left;
            color: black;
            font-family: sans-serif;
            font-size: 75%;

        }

        #xx{
            height: 80%;
            text-align: right top;
        }
        #j{
            right: 30px;
            position: absolute;
            top: 30px;
            height: 70%;
        }
    </style>
</head>
<body>
    <input type="color" name="" id="cl">
    <button onclick="cl()">RENK AYARLA</button>

    <div class="a">
        <h1 class="aktif" id="c">Ders Vakti</h1>
        <h1 class="pasif" id="m">Mola Vakti</h1>

        <p id="sayac">0:0</p>
    </div>
    <div>
        <h3 id="y">
            Toplam ders : 0   Toplam ders (dk) : 0 dk
        </h3>
    </div>
    <script>
        var calisma = document.getElementById("c");
        var mola = document.getElementById("m");
        var yd = document.getElementById("y");
        var sayac = document.getElementById("sayac");
        var calismasure = """+derssure+""";
        var saniye = 59;
        var molasure = """+tenefussure+""";
        var dakikac = calismasure-1;
        var dakikat = molasure-1;
        var calisilanderssayisi = 0;
        var dakika = dakikac;
        var sayi = 0;

        var yapilanders = "Toplam ders : " + calisilanderssayisi + "    Toplam ders (dk) : "+(calisilanderssayisi*calismasure)+" dk ";

        function dt(){
            dakika = dakikat;
            calisma.className = "pasif";
            mola.className = "aktif";
            calisilanderssayisi++;
            var yapilanders = "Toplam ders : " + calisilanderssayisi + "   Toplam ders (dk) : "+(calisilanderssayisi*calismasure)+" dk ";
            yd.innerHTML = yapilanders;
            saniye = 59;
        } 
        function td(){
            dakika = dakikac;
            calisma.className = "aktif";
            mola.className = "pasif";
            saniye = 59;

        }
        
        function f(){
            if(saniye>0){
                saniye--;
            }
            else if(saniye==0){
                if(dakika<0){
                 saniye = 59;
                 dakika--;

                }
                else if(sayi%2==0){
                    dt();
                    sayi++;
                }
                else{
                    td();
                    sayi++

                }
        
                
            }
            var s = dakika+":"+saniye;
            sayac.innerHTML = s;
        }
        setInterval(f,1000);
        function cl(){
            var cl = document.getElementById("cl").value;
            document.body.style.backgroundColor = cl;
        }


    </script"""+""">  
    <video controls  id="j">
        <source src='"""+self.video+"""' type="video/mp4">
    </video"""
            if(len(self.muzik1)>2)and(len(self.muzik2)>2)and(len(self.muzik3)>2):
             kod = kod + """>
    
    <audio src='"""+self.muzik1+"""' controls></audio>
    <br>
    <audio src='"""+self.muzik2+"""' controls></audio>
    <br>
    <audio src='"""+self.muzik3+"""' controls></audio>
</body>
</html>"""
            elif (len(self.muzik1)>2)and(len(self.muzik2)>2):
             kod = kod + """>
    
    <audio src='"""+self.muzik1+"""' controls></audio>
    <br>
    <audio src='"""+self.muzik2+"""' controls></audio>
</body>
</html>"""

            elif (len(self.muzik1)>2):
             kod = kod + """>
    
    <audio src='"""+self.muzik1+"""' controls></audio>
    
</body>
</html>"""
            else:
             kod = kod + """>
</body>
</html>"""

        else:
            kod = kod+""">
    <style>
        
        html{
            height: 100%;
        }
        body{
            height: 100%;
            background-color: aquamarine;
        }
        .a{
            
            text-align: center;
        }

        audio{
            
            color: rgb(52, 79, 81);
            size: 3cm;
            height: 15%;
            font-size: 2%;
            font-style: italic;
        }
        #sayac{
            color: black;
            
            
            font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
            font-weight: bold;
            text-align: center;
            text-shadow: 1px 1px 5px rgb(57, 71, 82);
            font-size : 225%
        }
        .aktif{
            text-shadow:1px 1px 15px rgb(255, 160, 160);
            color:rgb(255, 0, 0);
            text-align: center;
            font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
            font-size:450%;
            font-weight: bold;
        }
        .pasif{
            opacity: 0.5;
            color: rgb(191, 220, 246);
            text-align: center;
            font-size: 225%;
            font-weight: lighter;
        }
        #y{
            text-align: center;
            color: black;
            font-family: sans-serif;

        }
        button{
            padding: 7px 7px;
            font-size: 10px;
            color: aquamarine;
            background-color: black;
            font-family: 'Times New Roman', Times, serif;
            transition: 1s;
            opacity: 0.7; 
            
        }
        button:hover{
            font-size: 13px;
            color: green;
            background-color: aquamarine;
            scrollbar-shadow-color: aquamarine;
            box-shadow: 0.5px 0.5px 0.5px 0.5px,1px 1px 1px 1px,1.5px 1.5px 1.5px 1.5px;
            opacity: 1;
            font-style: bold;
        }
        
    </style>
</head>
<body>
    <input type="color" name="" id="cl">
    <button onclick="cl()">RENK AYARLA</button>
    
    <h1 class="aktif" id="c">Ders Vakti</h1>
    <h1 class="pasif" id="m">Mola Vakti</h1>

    <p id="sayac">0:0</p>

    
    <h3 id="y">
            Toplam ders : 0   Toplam ders (dk) : 0 dk
    </h3>
    
    <script>
        var calisma = document.getElementById("c");
        var mola = document.getElementById("m");
        var yd = document.getElementById("y");
        var sayac = document.getElementById("sayac");
        var calismasure = """+derssure+""";
        var saniye = 59;
        var molasure = """+tenefussure+""";
        var dakikac = calismasure-1;
        var dakikat = molasure-1;
        var calisilanderssayisi = 0;
        var dakika = dakikac;
        var sayi = 0;

        var yapilanders = "Toplam ders : " + calisilanderssayisi + "   Toplam ders (dk): "+(calisilanderssayisi*calismasure)+" dk ";

        function dt(){
            dakika = dakikat;
            calisma.className = "pasif";
            mola.className = "aktif";
            calisilanderssayisi++;
            var yapilanders = "Toplam ders : " + calisilanderssayisi + "    Toplam ders (dk) : "+(calisilanderssayisi*calismasure)+" dk ";
            yd.innerHTML = yapilanders;
            saniye = 59;
        } 
        function td(){
            dakika = dakikac;
            calisma.className = "aktif";
            mola.className = "pasif";
            saniye = 59;

        }
        
        function f(){
            if(saniye>0){
                saniye--;
            }
            else if(saniye==0){
                if(dakika<0){
                 saniye = 59;
                 dakika--;

                }
                else if(sayi%2==0){
                    dt();
                    sayi++;
                }
                else{
                    td();
                    sayi++

                }
        
                
            }
            var s = dakika+":"+saniye;
            sayac.innerHTML = s;
        }
        setInterval(f,1000);
        function cl(){
            var cl = document.getElementById("cl").value;
            document.body.style.backgroundColor = cl;
        }


    </script"""
           
            if(len(self.muzik1)>2)and(len(self.muzik2)>2)and(len(self.muzik3)>2):
             kod = kod+""">
    
    <audio src='"""+self.muzik1+"""' controls></audio>
    <audio src='"""+self.muzik2+"""' controls></audio>
    <audio src='"""+self.muzik3+"""' controls></audio>  
    
</body>
</html>"""

            elif(len(self.muzik1)>2)and(len(self.muzik2)>2):
             kod = kod+""">
    
    <audio src='"""+self.muzik1+"""' controls></audio>
    <audio src='"""+self.muzik2+"""' controls></audio>
</body>
</html>"""
            elif(len(self.muzik1)>2):
             kod = kod+""">
    
    <audio src='"""+self.muzik1+"""' controls></audio>
</body>
</html>"""
            else:
             kod = kod+""">
</body>
</html>"""


        yd = open("yskpomodoro.html","w")
        yd.write(kod)
        os.startfile("yskpomodoro.html")
        print(("Pomodoro başarıyla oluşturuldu Oluşturulma süresi : "+str((time.time()-ss))+"sn"))
        plus()


def ypomodoro(derssure,tenefussure):
    ss = time.time()
    sure = str(derssure)
    tsure = str(tenefussure)
    kod = """<!DOCTYPE html>
<html lang="tr">
<head>

    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content='width=device-width, initial-scale=1.0'>
    <style>
        
        html{
            height: 100%;
        }
        body{
            height: 100%;
            background-color: aquamarine;
        }
        .a{
            
            text-align: center;
        }

        audio{
            
            color: rgb(52, 79, 81);
            size: 3cm;
            height: 15%;
            font-size: 2%;
            font-style: italic;
        }
        #sayac{
            color: black;
            
            
            font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
            font-weight: bold;
            text-align: center;
            text-shadow: 1px 1px 5px rgb(57, 71, 82);
            font-size : 225%
        }
        button{
            padding: 7px 7px;
            font-size: 10px;
            color: aquamarine;
            background-color: black;
            font-family: 'Times New Roman', Times, serif;
            transition: 1s;
            opacity: 0.7; 
            
        }
        button:hover{
            font-size: 13px;
            color: green;
            background-color: aquamarine;
            scrollbar-shadow-color: aquamarine;
            box-shadow: 0.5px 0.5px 0.5px 0.5px,1px 1px 1px 1px,1.5px 1.5px 1.5px 1.5px;
            opacity: 1;
            font-style: bold;
        }
        .aktif{
            text-shadow:1px 1px 15px rgb(255, 160, 160);
            color:rgb(255, 0, 0);
            text-align: center;
            font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
            font-size:450%;
            font-weight: bold;
        }
        .pasif{
            opacity: 0.5;
            color: rgb(191, 220, 246);
            text-align: center;
            font-size: 225%;
            font-weight: lighter;
        }
        #y{
            text-align: center;
            color: black;
            font-family: sans-serif;

        }
        
    </style>
</head>
<body>
    <input type="color" name="" id="cl">
    <button onclick="cl()">RENK AYARLA</button>
    
    <h1 class="aktif" id="c">Ders Vakti</h1>
    <h1 class="pasif" id="m">Mola Vakti</h1>

    <p id="sayac">0:0</p>

    
    <h3 id="y">
            Toplam ders : 0   Toplam ders (dk) : 0 dk
    </h3>
    
    <script>
        var calisma = document.getElementById("c");
        var mola = document.getElementById("m");
        var yd = document.getElementById("y");
        var sayac = document.getElementById("sayac");
        var calismasure ="""+sure+""";
        var saniye = 59;
        var molasure = """+tsure+""";
        var dakikac = calismasure-1;
        var dakikat = molasure-1;
        var calisilanderssayisi = 0;
        var dakika = dakikac;
        var sayi = 0;

        var yapilanders = "Toplam ders : " + calisilanderssayisi + "   Toplam ders (dk): "+(calisilanderssayisi*calismasure)+" dk ";

        function dt(){
            dakika = dakikat;
            calisma.className = "pasif";
            mola.className = "aktif";
            calisilanderssayisi++;
            var yapilanders = "Toplam ders : " + calisilanderssayisi + "    Toplam ders (dk) : "+(calisilanderssayisi*calismasure)+" dk ";
            yd.innerHTML = yapilanders;
            saniye = 59;
        } 
        function td(){
            dakika = dakikac;
            calisma.className = "aktif";
            mola.className = "pasif";
            saniye = 59;

        }
        
        function f(){
            if(saniye>0){
                saniye--;
            }
            else if(saniye==0){
                if(dakika<0){
                 saniye = 59;
                 dakika--;

                }
                else if(sayi%2==0){
                    dt();
                    sayi++;
                }
                else{
                    td();
                    sayi++

                }
        
                
            }
            var s = dakika+":"+saniye;
            sayac.innerHTML = s;
        }
        setInterval(f,1000);
        function cl(){
            var cl = document.getElementById("cl").value;
            document.body.style.backgroundColor = cl;
        }


    </script>
</body>
</html>"""


    yd = open("yskpomodoro.html","w")
    yd.write(kod)
    os.startfile("yskpomodoro.html")
   
    
    
    print(("Pomodoro başarıyla oluşturuldu Oluşturulma süresi : "+str((time.time()-ss))+"sn"))
    
def hazirpomodoro():
    ss = time.time()
    sure = input("Ders süresini giriniz : ")
    tsure = input("Tenefüs süresini giriniz : ")
    kod = """<!DOCTYPE html>
<html lang="tr">
<head>

    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content='width=device-width, initial-scale=1.0'>
    <style>
        
        html{
            height: 100%;
        }
        body{
            height: 100%;
            background-color: aquamarine;
        }
        button{
            padding: 7px 7px;
            font-size: 10px;
            color: aquamarine;
            background-color: black;
            font-family: 'Times New Roman', Times, serif;
            transition: 1s;
            opacity: 0.7; 
            
        }
        button:hover{
            font-size: 13px;
            color: green;
            background-color: aquamarine;
            scrollbar-shadow-color: aquamarine;
            box-shadow: 0.5px 0.5px 0.5px 0.5px,1px 1px 1px 1px,1.5px 1.5px 1.5px 1.5px;
            opacity: 1;
            font-style: bold;
        }
        .a{
            
            text-align: center;
        }

        audio{
            
            color: rgb(52, 79, 81);
            size: 3cm;
            height: 15%;
            font-size: 2%;
            font-style: italic;
        }
        #sayac{
            color: black;
            
            
            font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
            font-weight: bold;
            text-align: center;
            text-shadow: 1px 1px 5px rgb(57, 71, 82);
            font-size : 225%
        }
        .aktif{
            text-shadow:1px 1px 15px rgb(255, 160, 160);
            color:rgb(255, 0, 0);
            text-align: center;
            font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
            font-size:450%;
            font-weight: bold;
        }
        .pasif{
            opacity: 0.5;
            color: rgb(191, 220, 246);
            text-align: center;
            font-size: 225%;
            font-weight: lighter;
        }
        #y{
            text-align: center;
            color: black;
            font-family: sans-serif;

        }
        
    </style>
</head>
<body>
    <input type="color" name="" id="cl">
    <button onclick="cl()">RENK AYARLA</button>
    
    <h1 class="aktif" id="c">Ders Vakti</h1>
    <h1 class="pasif" id="m">Mola Vakti</h1>

    <p id="sayac">0:0</p>

    
    <h3 id="y">
            Toplam ders : 0   Toplam ders (dk) : 0 dk
    </h3>
    
    <script>
        var calisma = document.getElementById("c");
        var mola = document.getElementById("m");
        var yd = document.getElementById("y");
        var sayac = document.getElementById("sayac");
        var calismasure ="""+sure+""";
        var saniye = 59;
        var molasure = """+tsure+""";
        var dakikac = calismasure-1;
        var dakikat = molasure-1;
        var calisilanderssayisi = 0;
        var dakika = dakikac;
        var sayi = 0;

        var yapilanders = "Toplam ders : " + calisilanderssayisi + "   Toplam ders (dk): "+(calisilanderssayisi*calismasure)+" dk ";
        function cl(){
            var cl = document.getElementById("cl").value;
            document.body.style.backgroundColor = cl;
        }
        function dt(){
            dakika = dakikat;
            calisma.className = "pasif";
            mola.className = "aktif";
            calisilanderssayisi++;
            var yapilanders = "Toplam ders : " + calisilanderssayisi + "    Toplam ders (dk) : "+(calisilanderssayisi*calismasure)+" dk ";
            yd.innerHTML = yapilanders;
            saniye = 59;
        } 
        function td(){
            dakika = dakikac;
            calisma.className = "aktif";
            mola.className = "pasif";
            saniye = 59;

        }
        
        function f(){
            if(saniye>0){
                saniye--;
            }
            else if(saniye==0){
                if(dakika<0){
                 saniye = 59;
                 dakika--;

                }
                else if(sayi%2==0){
                    dt();
                    sayi++;
                }
                else{
                    td();
                    sayi++

                }
        
                
            }
            var s = dakika+":"+saniye;
            sayac.innerHTML = s;
        }
        setInterval(f,1000);


    </script>
</body>
</html>"""


    yd = open("yskpomodoro.html","w")
    yd.write(kod)
    os.startfile("yskpomodoro.html")
    
    
    print(("Pomodoro başarıyla oluşturuldu Oluşturulma süresi : "+str((time.time()-ss))+"sn"))
    
def bilgi():
    print("""
    Hazırlayanlar : Ysk(0001)
    İletişim : https://discord.gg/y73bUJYfzY
    Ysk software iyi günler diler
    """)
    print("""Komutlar ::
    hazirpomodoro:consola gireceğiniz veriler ile basitçe pomodoro sayacı oluşturmanızı sağlar
    ypomodoro(derssüresi,tenefüssüresi):1.yere ders süresi yerine ders süresi 2.yere tenefus süresini yazınız program belirtilen ders ve tenefus suresinde pomodoro oluşturur
    pomodoro:pomodoro bir classtır
    pomodoro class'ının elemanları :
     1)muzik1 = yazarak ilk muziğin yolunu giriniz
     (daha fazla isterseniz muzik 2 muzik 3 seklinde devam edin)
     2)video = calısırken izlemek istediğiniz herhangi bir videonun yolunu giriniz
     3)pp projeye bir pp eklemek isterseniz fotoğrafın yolunu  giriniz
     4)baslik projeye başlık eklemek isterseniz baslığın yolunu giriniz
     5)derssure ders suresini giriniz
     6)tenefussure tenefus suresini girin
     7)basla projeyi baslatır
     8)elmas yazarak simdiye kadar kaç kez çalıştırdığınızı görüntüleyebilirsiniz
     *!projede baslik pp video muzik vb. isteğe bağlıdır girmeseniz de olur
     
    bilgi:proje hakkında bilgi verir""")
