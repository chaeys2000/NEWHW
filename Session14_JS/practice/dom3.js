const dc = document;
const mylist = dc.querySelector('.mylist');

for(let i=1; i<=3; i++) {
    let item = dc.createElement('li');
    item.innerText =i+" 번째 추가 항목";
    mylist.append(item);
}