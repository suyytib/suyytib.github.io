var code;  //在全局   
function createCode() {     //生成函数
  code = "";
  var codeLength = 6; //码的长度    
  var checkCode = document.getElementById("checkCode");   //获得一个对象  
  checkCode.value = "";
  var selectChar = new Array(1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z');

  for (var i = 0; i < codeLength; i++) {
    var charIndex = Math.floor(Math.random() * 100);
    //向下取整随机找字符
    code += selectChar[charIndex];
  }
  if (code.length != codeLength) {
    createCode(); //重新生成码
  }
  checkCode.value = code;
}


function validate() {    //比对函数
  var button = document.getElementById('myButton'); // 获取按钮元素
  button.value = 0;
  var inputCode = document.getElementById("input1").value.toUpperCase();//字母转大写来验证   
  var codeToUp = code.toUpperCase();
  if (inputCode.length <= 0) {
    alert("请输入验证码！");   //弹出信息    
  }
  else if (inputCode != codeToUp) {
    alert("验证码输入错误！");
    createCode();
  }
  else {
    button.value = 1;
  }

}       