// ADMIN
//------------- VIEW BILLINGS -------------//
$(document).ready(function(){
    $("#rButton").click(function(){
        $('#rentBillstbl').animate({height: 'toggle'}, 'fast');
    });
});
$(document).ready(function(){
    $("#eButton").click(function(){
        $('#eBillstbl').animate({height: 'toggle'}, 'fast');
    }); 
});
$(document).ready(function(){
    $("#wButton").click(function(){
        $('#wBillstbl').animate({height: 'toggle'}, 'fast');
    }); 
});
$(document).ready(function(){
    $("#wifiButton").click(function(){
        $('#wifiBillstbl').animate({height: 'toggle'}, 'fast');
    }); 
});

//------------- VIEW PAST BILLINGS -------------//
$(document).ready(function(){
    $('.pastBill button').click(function(){
        $('#pastbills').toggle().show();
        $('#bills').toggle().hide();       
    });
});

//------------- VIEW DROPDOWN -------------//
$(document).ready(function(){
    $("#tenantButton").click(function(){
        $('.unitlist').animate({height: 'toggle'}, 'fast', 'linear');
        $('#sub1, #sub2, #sub3, #sub4, #sub5, #sub6, #sub7, #sub8, #annInfo, #repInfo, #feedInfo, #billInfo, #Notifications').animate({height: 'hide'}, 'fast');
    }); 
});

//------------- VIEW TENANTS SUBMENUS -------------//
$(document).ready(function(){
    $("#unit1").click(function(){
        $('#sub1').animate({height: 'toggle'}, 'fast', 'linear');
        $('#sub2, #sub3, #sub4, #sub5, #sub6, #sub7, #sub8, #repInfo, #annInfo, #feedInfo, #billInfo, #Notifications').animate({height: 'hide'}, 'fast');
    });
});
$(document).ready(function(){
    $("#unit2").click(function(){
        $('#sub2').animate({height: 'toggle'}, 'fast', 'linear');
        $('#sub1, #sub3, #sub4, #sub5, #sub6, #sub7, #sub8, #repInfo, #annInfo, #feedInfo, #billInfo, #Notifications').animate({height: 'hide'}, 'fast');
    });
});
$(document).ready(function(){
    $("#unit3").click(function(){
        $('#sub3').animate({height: 'toggle'}, 'fast', 'linear');
        $('#sub1, #sub2, #sub4, #sub5, #sub6, #sub7, #sub8, #repInfo, #annInfo, #feedInfo, #billInfo, #Notifications').animate({height: 'hide'}, 'fast');
    });
});
$(document).ready(function(){
    $("#unit4").click(function(){
        $('#sub4').animate({height: 'toggle'}, 'fast', 'linear');
        $('#sub1, #sub2, #sub3, #sub5, #sub6, #sub7, #sub8, #repInfo, #annInfo, #feedInfo, #billInfo, #Notifications').animate({height: 'hide'}, 'fast');
    });
});
$(document).ready(function(){
    $("#unit5").click(function(){
        $('#sub5').animate({height: 'toggle'}, 'fast', 'linear');
        $('#sub1, #sub2, #sub3, #sub4, #sub6, #sub7, #sub8, #repInfo, #annInfo, #feedInfo, #billInfo, #Notifications').animate({height: 'hide'}, 'fast');
    });
});
$(document).ready(function(){
    $("#unit6").click(function(){
        $('#sub6').animate({height: 'toggle'}, 'fast', 'linear');
        $('#sub1, #sub2, #sub3, #sub4, #sub5, #sub7, #sub8, #repInfo, #annInfo, #feedInfo, #billInfo, #Notifications').animate({height: 'hide'}, 'fast');
    });
});
$(document).ready(function(){
    $("#unit7").click(function(){
        $('#sub7').animate({height: 'toggle'}, 'fast', 'linear');
        $('#sub1, #sub2, #sub3, #sub4, #sub5, #sub6, #sub8, #repInfo, #annInfo, #feedInfo, #billInfo, #Notifications').animate({height: 'hide'}, 'fast');
    });
});
$(document).ready(function(){
    $("#unit8").click(function(){
        $('#sub8').animate({height: 'toggle'}, 'fast', 'linear');
        $('#sub1, #sub2, #sub3, #sub4, #sub5, #sub6, #sub7, #repInfo, #annInfo, #feedInfo, #billInfo, #Notifications').animate({height: 'hide'}, 'fast');
    });
});


// -------------- MODAL --------------//
$(document).ready(function(){
    $('.minusButton').click(function(){
        var currentRow=$(this).closest(".submenu tr");
        tenantName = currentRow.find('td:eq(0)').text();
        tenantMobile = currentRow.find('td:eq(1)').text();  
        $('.modal, #remove_move').show();

        $('#remove').click(function(){
            $.post("/admin/remove",
                {nameToRemove: tenantName, mobileToRemove: tenantMobile},
                function(){});
        });

        $('#closeBtn').click(function(){
            $('.modal, #remove_move').hide();
        });
    });

});


// -------------- CHANGE STATUS OF PAYMENT IN TENANTS --------------//
// $(document).ready(function(){
//     $('#confirm_notif').click(function(){
//         var currentRow=$(this).closest(".submenu ");
//         inRow = currentRow.find('td:eq(3)').text();
        // nameInRow = JSON.stringify(inRow);
        // alert(inRow);
        // $('.modal, #remove_move').show();
    // });
    // $('#remove').click(function(){
    //     $.post("/remove", { inRow: inRow }, 'application/json');

    // });
    // $('#closeBtn').click(function(){
    //     $('.modal, #remove_move').hide();
    // });
// });



//------------- VIEW ANNOUNCEMENTS -------------//
// $(window).on('load', function(){
//     $('#alert').fadeIn().fadeOut(3000);
// });

$(document).ready(function(){
    $("#annButton").click(function(){
        $('#annInfo').animate({height: 'toggle'}, 'fast', 'linear');
        $('#sub1, #sub2, #sub3, #sub4, #sub5, #sub6, #sub7, #sub8, #unitinfo, #repInfo, #feedInfo, #billInfo, #Notifications').animate({height: 'hide'}, 'fast');
    });
});

//------------- VIEW NOTIFICATIONS -------------//
$(document).ready(function(){
    $("#homeButton").click(function(){
        $('#Notifications').animate({height: 'toggle'}, 'fast', 'linear');
        $('#sub1, #sub2, #sub3, #sub4, #sub5, #sub6, #sub7, #sub8, #unitinfo, #annInfo, #repInfo, #billInfo, #feedInfo').animate({height: 'hide'}, 'fast');
    });
});

//------------- VIEW REPORTS -------------//
$(document).ready(function(){
    $("#repButton").click(function(){
        $('#repInfo').animate({height: 'toggle'}, 'fast', 'linear');
        $('#sub1, #sub2, #sub3, #sub4, #sub5, #sub6, #sub7, #sub8, #unitinfo, #annInfo, #feedInfo, #billInfo, #Notifications').animate({height: 'hide'}, 'fast');
    });
});

//------------- VIEW FEEDBACKS -------------//
$(document).ready(function(){
    $("#feedButton").click(function(){
        $('#feedInfo').animate({height: 'toggle'}, 'fast', 'linear');
        $('#sub1, #sub2, #sub3, #sub4, #sub5, #sub6, #sub7, #sub8, #unitinfo, #annInfo, #repInfo, #billInfo, #Notifications').animate({height: 'hide'}, 'fast');
    });
});

//------------- SEND BILLS -------------//
$(document).ready(function(){
    $("#sendBill").click(function(){
        $('#billInfo').animate({height: 'toggle'}, 'fast', 'linear');
        $('#sub1, #sub2, #sub3, #sub4, #sub5, #sub6, #sub7, #sub8, #unitinfo, #annInfo, #repInfo, #feedInfo, #Notifications').animate({height: 'hide'}, 'fast');
    });
});

//--------------------- FADE IN AND FADE OUT OF USER MENU -------------------------//
function showMenu(){
    x = document.getElementById("container");
       if (x.style.display == 'none') {
        x.style.display = 'block';
    } else {
        x.style.display = 'none'; } 
        
    var insert = true;
    let div = document.getElementById("container");

    if (insert == true) {
        div.style.animation = "fadein 1s";
        insert = false;
    }
    // else if (insert == false) {
    //     div.style.animation = "fadeout 1s";
    //     insert = true;
    // }
}

//--------------------- SHOW MENU  -------------------------// 

$(document).ready(function(){
    $("#profile").click(function(){
        $('#Profile').animate({height: 'toggle'}, 'fast', 'linear');
        $('#Payments, #Announcement, #Report, #Feedback, #Notification').animate({height: 'hide'}, 'fast');
    });
    $("#notification").click(function(){
        $('#Notification').animate({height: 'toggle'}, 'fast', 'linear');
        $('#Payments, #Announcement, #Report, #Feedback, #Profile').animate({height: 'hide'}, 'fast');
    });
    $("#payments").click(function(){
        $('#Payments').animate({height: 'toggle'}, 'fast', 'linear'); 
        $('#Profile, #Announcement, #Report, #Feedback, #Notification').animate({height: 'hide'}, 'fast');
    });
    $("#announce").click(function(){
        $('#Announcement').animate({height: 'toggle'}, 'fast', 'linear');
        $('#Profile, #Payments, #Report, #Feedback, #Notification').animate({height: 'hide'}, 'fast');
    });
    $("#report").click(function () {
        $("#Report").animate({height: 'toggle'}, 'fast', 'linear');
        $('#Payments, #Announcement, #Profile, #Feedback, #Notification').animate({height: 'hide'}, 'fast');
    });
    $("#feedback").click(function () {
        $("#Feedback").animate({height: 'toggle'}, 'fast', 'linear');
        $('#Payments, #Announcement, #Profile, #Report, #Notification').animate({height: 'hide'}, 'fast');
    });
    $("#change_icon").click(function(){
                randomize();
    });
});

//--------------------- Notification icon change -------------------------//

// $(document).ready(function(){
//     if (admin_notif_count>0) {
//         alert("there is a notification")
//         $("#homeButton").css("color", "red");
//     };

//     if (admin_notif_count>0) {
//         $("#notif_icon").css("color", "red");
//     };
// });

//--------------------- SHOW EDIT PROFILE -------------------------//

// $(document).ready(function(){
    // $("#edit_profile").click(function(){
    //     $('#upper1 input').removeAttr('disabled');
    //     $.get('/update',{
    //         user_fullname: $('input[name="user_fullname"]').val(),
    //         user_address: $('input[name="user_address"]').val(),
    //         user_mobile: $('input[name="user_mobile"]').val(),
    //         user_guardian: $('input[name="user_guardian"]').val(),
    //         user_guardian_num: $('input[name="user_guardian_num"]').val(),
    //         user_school: $('input[name="user_school"]').val(),
    //         user_year: $('input[name="user_year"]').val(),
    //         user_email: $('input[name="user_email"]').val()
    //     }, function(){});
    // });
    // $("#save_profile").click(function(){
    //     $('#upper1 input').attr('disabled', 'disabled');
        // $.post("/update",
        //     {user_fullname: $('input[name="user_fullname"]').val(),
        //     user_address: $('input[name="user_address"]').val(),
        //     user_mobile: $('input[name="user_mobile"]').val(),
        //     user_guardian: $('input[name="user_guardian"]').val(),
        //     user_guardian_num: $('input[name="user_guardian_num"]').val(),
        //     user_school: $('input[name="user_school"]').val(),
        //     user_year: $('input[name="user_year"]').val(),
        //     user_email: $('input[name="user_email"]').val()
        //     },
        //     function(data, status, jqXHR) {// success callback
        //             $('#welcome').append('status: ' + status + ', data: ' + data);
        //     });
        // $.post('/update',   // url
        // {user_fullname: $('#uname').val(),
        // user_address: $('#uadd').val(),
        // user_mobile: $('#umob').val(),
        // user_guardian: $('#uguard').val(),
        // user_guardian_num: $('#uguardnum').val(),
        // user_school: $('#uschool').val(),
        // user_year: $('#uyear').val(),
        // user_email: $('#email').val()}, // data to be submit
        // function(data, status, jqXHR) {// success callback
        //             $('#welcome').append('status: ' + status + ', data: ' + data);
        //     });
//     });
//     $("#change_icon").click(function(){
//         randomize();
//     });
// });

var icon_collection = new Array("/static/images/icons/icon-1.jpg","/static/images/icons/icon-2.jpg","/static/images/icons/icon-3.jpg",
"/static/images/icons/icon-4.jpg", "/static/images/icons/icon-5.jpg", "/static/images/icons/icon-6.jpg", "/static/images/icons/icon-7.jpg",
"/static/images/icons/icon-8.jpg", "/static/images/icons/icon-9.jpg");

function randomize() {
    var randomNum = Math.floor(Math.random() * icon_collection.length);
    document.getElementById("icons").src = icon_collection[randomNum]; }
    
//--------------------- Payment Radio Button -------------------------//
$(document).ready(function(){
    $('#gcash1').click(function(){
        $('#payPerson1').animate({height: 'hide'}, 'fast');
        $('#payGcash1').animate({height: 'toggle'}, 'fast', 'linear');

    });
    $('#payPersonal1').click(function(){
        $('#payGcash1').animate({height: 'hide'}, 'fast');
        $('#payPerson1').animate({height: 'toggle'}, 'fast', 'linear');
    });
    $('#gcash2').click(function(){
        $('#payPerson2').animate({height: 'hide'}, 'fast');
        $('#payGcash2').animate({height: 'toggle'}, 'fast', 'linear');

    });
    $('#payPersonal2').click(function(){
        $('#payGcash2').animate({height: 'hide'}, 'fast');
        $('#payPerson2').animate({height: 'toggle'}, 'fast', 'linear');
    });
    $('#gcash3').click(function(){
        $('#payPerson3').animate({height: 'hide'}, 'fast');
        $('#payGcash3').animate({height: 'toggle'}, 'fast', 'linear');

    });
    $('#payPersonal3').click(function(){
        $('#payGcash3').animate({height: 'hide'}, 'fast');
        $('#payPerson3').animate({height: 'toggle'}, 'fast', 'linear');
    });
    $('#gcash4').click(function(){
        $('#payPerson4').animate({height: 'hide'}, 'fast');
        $('#payGcash4').animate({height: 'toggle'}, 'fast', 'linear');

    });
    $('#payPersonal4').click(function(){
        $('#payGcash4').animate({height: 'hide'}, 'fast');
        $('#payPerson4').animate({height: 'toggle'}, 'fast', 'linear');
    });
});

// User billings
$(document).ready(function(){
    $("#rpButton").click(function(){
        $('#rentpBillstbl').animate({height: 'toggle'}, 'fast');
    });
});
$(document).ready(function(){
    $("#epButton").click(function(){
        $('#epBillstbl').animate({height: 'toggle'}, 'fast');
    }); 
});
$(document).ready(function(){
    $("#wpButton").click(function(){
        $('#wpBillstbl').animate({height: 'toggle'}, 'fast');
    }); 
});
$(document).ready(function(){
    $("#wifipButton").click(function(){
        $('#wifipBillstbl').animate({height: 'toggle'}, 'fast');
    }); 
});

//--------------------- Confirm if rent is paid -------------------------//
// $(document).ready(function(){
//     $('#payments').click(function(){
//         alert(isPaid);
//     //     $.post('/paymentCheck',   // url
//     //    { myData: 'This is my data.' }, // data to be submit
//     //    function(data, status, jqXHR) {// success callback
//     //             $('p').append('status: ' + status + ', data: ' + data);
//     //     });
//     });
// });



//--------------------- Confirm pay click, view button disable -------------------------//
// $(document).ready(function(){
//     $('#confirmRent').click(function(){
//         $('#rpButton').attr('disabled', 'disabled');
//     });
// });

// var username = '{{ data.username|tojson }}'
//         var site = {{ data.site }}