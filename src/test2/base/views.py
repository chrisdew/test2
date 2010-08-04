# Create your views here.
from django.http import HttpResponse
from PIL import Image, ImageColor, ImageFont, ImageDraw
     
#def sprite(request):    
#    return HttpResponse("hello world")
    
def sprite( request
          , gender="m"
          , hair="01"
          , pants="01"
          , shoes="01"
          , top="01"
          ):
    #bgcolor = ImageColor.getrgb("#" + color);

    width = 200
    height = 340
    image = Image.new("RGBA", (width, height), (0,0,0,0))
    
    #font = ImageFont.truetype("/usr/share/fonts/truetype/ttf-dejavu/DejaVuSansMono-Bold.ttf", 11)
    draw = ImageDraw.Draw(image)
    
    response = HttpResponse(mimetype="image/png")
    image.save(response, "PNG")
    return response
