$(function () {

  'use strict';

  var console = window.console || { log: function () {} };
  var $image = $('#image'); 

  $image.cropper({
    aspectRatio: 1 / 1,
    autoCropArea: 0,
    strict: false,
    guides: false,
    highlight: true,
    dragCrop: false,
    cropBoxMovable: false,
    cropBoxResizable: false,
    built: function () {
      // Width and Height params are number types instead of string
      $image.cropper("setCropBoxData", { width: window.innerWidth  });
      $image.cropper("setCanvasData", { left:0, width: window.innerWidth, height: 800 });
    }
  });
 
    // Methods for moblie
  $('.docs-buttons').on('touchstart', '[data-method]', function () {
    var $this = $(this);
    var data = $this.data();
    var $target;
    var result;

    if ($this.prop('disabled') || $this.hasClass('disabled')) {
      return;
    }

    if ($image.data('cropper') && data.method) {
      data = $.extend({}, data); // Clone a new one

      if (typeof data.target !== 'undefined') {
        $target = $(data.target);
        if (typeof data.option === 'undefined') {
          try {
            data.option = JSON.parse($target.val());
          } catch (e) {
            console.log(e.message);
          }
        }
      }

      result = $image.cropper(data.method, data.option, data.secondOption);

      switch (data.method) {
        case 'scaleX':
        case 'scaleY':
          $(this).data('option', -data.option);
          break;

        case 'getCroppedCanvas':
          if (result) {
                   $image.cropper('getCroppedCanvas').toBlob(function (blob) {
                                    var formData = new FormData();
                                    var id_kb = $('#id_kbid').val(); 
                                    formData.append('imagefile', blob);  
                                    formData.append("id_kb", id_kb); 

                                    $.ajax('/kb/save_kb_top_pic/', {
                                        method: "POST",
                                        data: formData,
                                        processData: false,
                                        contentType: false,
                                        success: function (data) {
                                        if (data['status'] == 'OK') {
                                                $().message(data['msg']);
                                                var delay = 3000; //delay in milliseconds
                                                //去查看帖子详情 
                                                setTimeout(function() { 
                                                    window.location.href = '/kb/'+data['id_kb']+'/kb_detail/'; }, delay);
                                            }
                                            else {
                                                $('.div_err').append('<label class="err_label" >' + data['msg'] + '</label>'); //
                                            }
                                        },
                                        error: function () {
                                        console.log('Upload error');
                                        }
                                    });
                     });      
          
          }

          break;
      }

      if ($.isPlainObject(result) && $target) {
        try {
          $target.val(JSON.stringify(result));
        } catch (e) {
          console.log(e.message);
        }
      }

    }
  });
  

  // Keyboard
  $(document.body).on('keydown', function (e) {

    if (!$image.data('cropper') || this.scrollTop > 300) {
      return;
    }

    switch (e.which) {
      case 37:
        e.preventDefault();
        $image.cropper('move', -1, 0);
        break;

      case 38:
        e.preventDefault();
        $image.cropper('move', 0, -1);
        break;

      case 39:
        e.preventDefault();
        $image.cropper('move', 1, 0);
        break;

      case 40:
        e.preventDefault();
        $image.cropper('move', 0, 1);
        break;
    }

  });


  // Import image
  var $inputImage = $('#inputImage');
  var URL = window.URL || window.webkitURL;
  var blobURL;

  if (URL) {
    $inputImage.change(function () {
      var files = this.files;
      var file;

      if (!$image.data('cropper')) {
        return;
      }

      if (files && files.length) {
        file = files[0];

        if (/^image\/\w+$/.test(file.type)) {
          blobURL = URL.createObjectURL(file);
          $image.one('built.cropper', function () {

            // Revoke when load complete
            URL.revokeObjectURL(blobURL);
          }).cropper('reset').cropper('replace', blobURL);
          $inputImage.val('');
        } else {
          window.alert('Please choose an image file.');
        }
      }
    });
  } else {
    $inputImage.prop('disabled', true).parent().addClass('disabled');
  }

});

  