const romanToInt = function(arr) {
    s = arr.split('')
    const values = {I: 1, V: 5, X: 10, L: 50, C: 100, D: 500, M: 1000}
    num = 0
    for(let i = 0; i <= s.length-1; i++){
        if (s[i] === 'I' && s[i+1] == 'V' || s[i] === 'I' && s[i+1] == 'X'){
            num = num + (values[s[i+1]] - values[s[i]])
            console.log(values[s[i+1]] - values[s[i]])
        } else if (s[i] === 'X' && s[i+1] == 'L' || s[i] === 'X' && s[i+1] == 'C'){
            num = num + (values[s[i+1]] - values[s[i]])
            console.log(values[s[i+1]] - values[s[i]])
        } else if (s[i] === 'C' && s[i+1] == 'D' || s[i] === 'C' && s[i+1] == 'M'){
            num = num + (values[s[i+1]] - values[s[i]])
            console.log(values[s[i+1]] - values[s[i]])
        }
    }
    console.log(num)
    let result = 0
    for(let i=0; i <= s.length-1; i++){
        if (s[i] === 'I' && s[i+1] == 'V' || s[i] === 'I' && s[i+1] == 'X'){
            i++
            continue
        } else if (s[i] === 'X' && s[i+1] == 'L' || s[i] === 'X' && s[i+1] == 'C'){
            i++
            continue
        } else if (s[i] === 'C' && s[i+1] == 'D' || s[i] === 'C' && s[i+1] == 'M'){
            i++
            continue
        } else{
            console.log(values[s[i]])
            result += values[s[i]]
        }
    }
    return result + num
};