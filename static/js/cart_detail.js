
function delRow(){
        var $obj = $("input[name='chk']");
        var checkCount = $obj.size();
        if($("input[name='chk']:checked").length===0){
            alert("삭제할 상품을 선택해주세요.");
        }
        else{
            for (var i=0; i<checkCount; i++){
                if($obj.eq(i).is(":checked")){
                    $obj.eq(i).parent().parent().remove();

                    var del_id = $obj.eq(i).parent().parent().attr('data-itemId');
                    let param ={
                        'del_id': del_id,
                    };
                    $.ajax({
                        url : del_cart,
                        type: 'POST',
                        datatype: 'json',
                        contentType: 'application/json; charset=utf-8',
                        data: JSON.stringify(param),
                        headers: {
                            'X-CSRFTOKEN' : '{{ csrf_token }}'
                        },
                        success : function(data) {
                        console.log("delete success");
                        },
                        error: function(data) {
                        alert("error= cart");
                        }
                    });
                }
            }
        }
        location.reload();
    };


function delAllRow(){
        var $obj = $("input[name='chk']");
        var checkCount = $obj.size();
        for (var i=0; i<checkCount; i++){
            $obj.eq(i).parent().parent().remove();
            var del_userId = $obj.eq(i).parent().parent().attr('data-userId');
            }
        let param ={
            'del_userId': del_userId,
        };
        $.ajax({
            url : del_all_cart,
            type: 'POST',
            datatype: 'json',
            contentType: 'application/json; charset=utf-8',
            data: JSON.stringify(param),
            headers: {
                'X-CSRFTOKEN' : '{{ csrf_token }}'
            },
            success : function(data) {
            console.log("delete all success");
            alert("장바구니를 비웠습니다.");
            },
            error: function(data) {
            alert("error= delete all");
            }
        });
        location.reload();
    };


$('.quantity').bind('change', function() {
        <!--변수에 값 담기-->
        var proName = $(this).parent().prev().prev().text();
        var proPrice = $(this).parent().prev().text();
        var proQuantity = $(this).val();
        var proAmount = $(this).parent().next().text();
        var proId = $(this).parent().next().next().val();
        var stock = $(this).parent().next().next().next().val();
        var ordId = $(this).parent().next().next().next().next().val();

        <!--정수형 변환-->
        var proPrice = Number(proPrice);
        var proQuantity = Number(proQuantity);

        <!--ajax 값 넘기기-->
        let order_pro_id = proId;
        let order_quantity = proQuantity;
        let order_id = ordId;
        let param = {
            'order_pro_id': order_pro_id,
            'order_quantity': order_quantity,
            'order_id': order_id,
        }
        $.ajax({
            url : update_cart,
            type: 'POST',
            datatype: 'json',
            contentType: 'application/json; charset=utf-8',
            data: JSON.stringify(param),
            headers: {
                'X-CSRFTOKEN' : '{{ csrf_token }}'
            },
            success : function(data) {
              console.log("update success");
            },
            error: function(data) {
              alert("error= cart");
            }
        });

        <!--수량에 따라 합계 바꾸기-->
        $(this).parent().next().text(proQuantity*proPrice);
        <!--총 합계 바꾸기-->
        location.reload();
    });



    //본 예제에서는 도로명 주소 표기 방식에 대한 법령에 따라, 내려오는 데이터를 조합하여 올바른 주소를 구성하는 방법을 설명합니다.
function sample4_execDaumPostcode() {
    new daum.Postcode({
        oncomplete: function(data) {
            // 팝업에서 검색결과 항목을 클릭했을때 실행할 코드를 작성하는 부분.

            // 도로명 주소의 노출 규칙에 따라 주소를 표시한다.
            // 내려오는 변수가 값이 없는 경우엔 공백('')값을 가지므로, 이를 참고하여 분기 한다.
            var roadAddr = data.roadAddress; // 도로명 주소 변수
            var extraRoadAddr = ''; // 참고 항목 변수

            // 법정동명이 있을 경우 추가한다. (법정리는 제외)
            // 법정동의 경우 마지막 문자가 "동/로/가"로 끝난다.
            if(data.bname !== '' && /[동|로|가]$/g.test(data.bname)){
                extraRoadAddr += data.bname;
            }
            // 건물명이 있고, 공동주택일 경우 추가한다.
            if(data.buildingName !== '' && data.apartment === 'Y'){
               extraRoadAddr += (extraRoadAddr !== '' ? ', ' + data.buildingName : data.buildingName);
            }
            // 표시할 참고항목이 있을 경우, 괄호까지 추가한 최종 문자열을 만든다.
            if(extraRoadAddr !== ''){
                extraRoadAddr = ' (' + extraRoadAddr + ')';
            }

            // 우편번호와 주소 정보를 해당 필드에 넣는다.
            document.getElementById('sample4_postcode').value = data.zonecode;
            document.getElementById("sample4_roadAddress").value = roadAddr;
            document.getElementById("sample4_jibunAddress").value = data.jibunAddress;

            // 참고항목 문자열이 있을 경우 해당 필드에 넣는다.
            if(roadAddr !== ''){
                document.getElementById("sample4_extraAddress").value = extraRoadAddr;
            } else {
                document.getElementById("sample4_extraAddress").value = '';
            }

            var guideTextBox = document.getElementById("guide");
            // 사용자가 '선택 안함'을 클릭한 경우, 예상 주소라는 표시를 해준다.
            if(data.autoRoadAddress) {
                var expRoadAddr = data.autoRoadAddress + extraRoadAddr;
                guideTextBox.innerHTML = '(예상 도로명 주소 : ' + expRoadAddr + ')';
                guideTextBox.style.display = 'block';

            } else if(data.autoJibunAddress) {
                var expJibunAddr = data.autoJibunAddress;
                guideTextBox.innerHTML = '(예상 지번 주소 : ' + expJibunAddr + ')';
                guideTextBox.style.display = 'block';
            } else {
                guideTextBox.innerHTML = '';
                guideTextBox.style.display = 'none';
            }
        }
    }).open();
}


