function get_captcha() {
  // 监听id为button函数的点击事件
  $("#button").click(function (event) {
    var $this = $(this);
    // 阻止默认事件
    event.preventDefault();
    // 获取邮箱信息
    var email = $("input[name='email']").val();
    $.ajax({
      url: "/login/register/email_send/?email=" + email,
      method: "GET",
      success: function (result) {
        // 获取result中的code值,其中result值是访问的python视图函数的返回的json数据
        var code = result["code"];
        if (code == 200) {
          var time = 60;
          $this.off("click"); // 禁止监听按钮功能
          var timer = setInterval(function () {
            //设置计时器
            $this.text(time); // 将缓冲时间显示在按钮文本上
            time -= 1;
            if (time <= 0) {
              clearInterval(timer); //清楚计时器
              $this.text("获取验证码"); //回复按钮文本
              get_captcha(); //重新开始监听指定id的按钮(通过重新执行该函数实现)
            }
          }, 1000);
        } else {
          alert("发送异常!");
        }
      },
      error: function (error) {
        alert("发送请求失败!");
      },
    });
  });
}
$(function () {
  // 延迟函数在网页在加载完毕后执行
  get_captcha();
});
