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
    path = "/srv/test2/static/images/half-kaizer/" + gender + "/"
    skin = Image.open(path + "skin/" + "01.png")
    hair = Image.open(path + "hair/" + hair + ".png")
    pants = Image.open(path + "pants/" + pants + ".png")
    shoes = Image.open(path + "shoes/" + shoes + ".png")
    top = Image.open(path + "top/" + top + ".png")
    
    image.paste(skin, None, skin)
    image.paste(hair, None, hair)
    image.paste(pants, None, pants)
    image.paste(shoes, None, shoes)
    image.paste(top, None, top)
    
    response = HttpResponse(mimetype="image/png")
    image.save(response, "PNG")
    return response
