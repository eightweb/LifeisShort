

//  js 的闭包
function fa() {
  age = 18;
  function son(name) { 
    console.log(`${name}, ===>> ${age}`)
   }
   return son
}

age  = 28
let f = fa()

f('xiaohong')