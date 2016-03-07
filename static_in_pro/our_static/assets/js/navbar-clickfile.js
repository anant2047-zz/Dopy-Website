function menuScript(){
        var fileref = document.createElement('script');
        fileref.setAttribute("type","type/javascript");
        fileref.setAttribute("src","https://code.jquery.com/jquery-1.10.2.min.js");

        var fileref1 = document.createElement('script');
        fileref1.setAttribute("type","type/javascript");
        fileref1.setAttribute("src","{% static "assets/js/main.js" %}");
        //$( ".link" ).append("<script src='https://code.jquery.com/jquery-1.10.2.min.js'></script>");
      }