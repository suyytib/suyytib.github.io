var ans='';
function choujiang() {
    var anseron = document.getElementById("anseron"); 
    anseron.value="";
    const cj = new Promise((resolve, reject) => {
        setTimeout((a) => {
            a = Math.floor(Math.random() * 101);
            ans+=`本次抽取的随机数:${a},`;
            if (a > 60) {
                resolve(a);
            } else {
                reject('再接再厉');
            }
        }, 0);
    })
    cj.then((resolve) => {
        ans+=`数值为${resolve}%,抽奖成功!笔记本电脑1台!`;
    })
        .catch((error) => {
            ans+=`抽奖失败,${error}`;
        })
    anseron.value = ans;
    ans='';
}
$(function () {
    // 延迟函数在网页在加载完毕后执行
    choujiang();
  });