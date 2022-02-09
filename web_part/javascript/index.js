// console.log('Heolo codeit!')
// console.log(10 + 5);console.log(7+8)
// //comment 다는 법
// /*
// 다중 comment 사용하는법
// */
// //변수선언
// var espressoPrice = 3000;
// var mochaPrice = 4000;
// console.log("coffee : "+ espressoPrice)
// console.log(mochaPrice)

//함수 선언
// function greetings(sentence){
//     console.log("HI")
//     console.log("안녕")
//     console.log("Bonjour")
//     console.log(sentence)
// };

// function welcome(name){
//     console.log('안녕하세요 ' + name + ' 님!');
// }

// function square(x){
//     console.log(x*x)
// }

// function printsum(a, b){
//     console.log(a+b)
// }

// function introduce(name, birth, nation, job){
//     console.log("이름 : " + name);
//     console.log("생년월일 : " + birth);
//     console.log("국적 : " + nation);
//     console.log("직업 : " + job);
// }

// var codeit = {
//     name: 'code',
//     year: '2017',
//     nice: true,
//     'worst course': null,
//     nicecourse: {
//         title: 'javascript programming',
//         language : 'javascript'
//     }
// };



// greetings("hola");
// welcome("james")
// square(3)
// printsum(10,5)
// introduce('code', '08.05.15', 'korea', 'student')
// console.log(typeof {
//     brandname: 'code', bornyear: 2017, isverynice: true, worstcourse: null,
//     bsetcourse: { title: '자바스크립트 프로그래밍 기초', language: 'javascript'}
// }) //결과값은 object
// //점표기법
// console.log(codeit.year) 
// //대괄호 표기법
// console.log(codeit['worst course'])
// var property = 'name';
// console.log(codeit[property])
// console.log(codeit.ceo); //undefined
// codeit.ceo = 'Gang';  
// // console.log(codeit.ceo);
// // devare codeit.nice;
// // console.log(codeit.nice)
// console.log(codeit.name !== undefined); //존재여부 확인
// console.log('name' in codeit); //undefined 값이 할당될 수도 있기 떄문에 안전하게 in 사용
// if('name' in codeit) {
//     console.log(`name 값은 ${codeit.name}입니다`);
// } else {
//     console.log('name 프로퍼티는 존재하지 않습니다.')
// }
// alert(10+20+ '!!!!')
// var number = 10;
// alert(++number);
// alert(++number);
// alert(++number);


// var test = function ( ) { return 10 } //function ( ) { return 10 }
// function text() { return 20 }
// alert(test()) //10
// // "123"
// for (var i = 10; i >=0;) {
//     alert(i);
//     i -= 3;
// }

// for (var i = 1; i <= 10; i++) {
//     if(i%5 == 0) {
//         alert(i);
//     }
// }

// for (var i = 0; i < 5; i++) {
//     for (var j = 0; j <= i; j++) {
//     alert('*');
//     }
//     alert('\n');
// }
// var star = '';

// for ( var i = 1 ; i < 10 ; i ++){
// 	for (var j = 0 ; j < i ; j++){
// 		star += '*';
// 	}	

// 	star += '\n';
// }
// alert(star);




// for (var i = 1; i <= 10; i++) {
//     if (i%5 == 0) {
//         alert(i);
//     }
// }
// var i = 1;
// while(i <=10) {
//     i +=1;
//     if( i%5 == 0) {
//         alert(i);
//     }
// }

// var input = prompt("입력하세요 : ", " ");
// alert(parseInt(input/1000));
// alert(parseInt(input%1000/100));
// alert(parseInt(input%100/10));
// alert(parseInt(input%10));

// var input = prompt("연도를 입력하시오", " ");
// if (input%12 == 0) {
//     alert("원숭이띠");
// } else {
//     if (input%12 == 1) {
//         alert("닭띠");
//     } else {
//         if (input%12 == 2) {
//             alert("개띠");
//         } else {
//             if (input%12 == 3) {
//                 alert("돼지띠");
//             } else {
//                 if (input%12 == 4) {
//                     alert("쥐띠");
//                 } else {
//                     if (input%12 == 5) {
//                         alert("소띠");
//                     } else {
//                         if (input%12 == 6) {
//                             alert("범띠");
//                         } else {
//                             if (input%12 == 7) {
//                                 alert("토끼띠");
//                             } else {
//                                 if (input%12 == 8) {
//                                     alert("용띠");
//                                 } else {
//                                     if (input%12 == 9) {
//                                         alert("뱀띠");
//                                     } else {
//                                         if (input%12 == 10) {
//                                             alert("말띠");
//                                         } else {
//                                             if (input%12 == 11) {
//                                                 alert("양띠");
//                                             }
//                                         }
//                                     }
//                                 }
//                             }
//                         }
//                     }
//                 }
//             }
//         }
//     }
// } 

var product = {
    이름 : "C# 프로그래밍(2판)",
    "초판 발행" : "2019년 12월 10일",
    지은이 : "윤인선",
    펴낸이 : "김태현",
    펴낸곳 : "한빛아카데미(주)",
    책임편집 : "변소현",
    기획 : "김성무",
    편집 : "김성무",
    디자인 : "김연정"
};
for ( var i in product) {
    document.write(i + ":" + product[i] +"<br>");
}

// var cm = prompt("CM 를 입력하시오");
// var inch;
// var feet;

// inch=2.54*cm;
// feet=12*inch;

// alert('inch는'+inch+" feet는 "+feet);

// if (x> 10) {
//     if(x < 20) {
//         alert(x);
//     }
// }
alert(10/0);
// i = 10;
// while (i >= 0) {
//     alert(i)
//     i -=3;
// }
