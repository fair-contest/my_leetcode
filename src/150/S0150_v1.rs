impl Solution {
    pub fn eval_rpn(tokens: Vec<String>) -> i32 {
        if tokens.len() == 1 { return tokens[0].parse::<i32>().unwrap()}
        let mut sp = vec![];
        for i in tokens.iter() {
            match i as &str {
                "+" => { let mut tmp = sp.pop().unwrap() as i32; tmp = sp.pop().unwrap() as i32 + tmp; sp.push(tmp); },
                "-" => { let mut tmp = sp.pop().unwrap() as i32; tmp = sp.pop().unwrap() as i32 - tmp; sp.push(tmp); },
                "*" => { let mut tmp = sp.pop().unwrap() as i32; tmp = sp.pop().unwrap() as i32 * tmp; sp.push(tmp); },
                "/" => { let mut tmp = sp.pop().unwrap() as i32; tmp = sp.pop().unwrap() as i32 / tmp; sp.push(tmp); },
                _ => sp.push(i.parse::<i32>().unwrap()),
            }
        }
        sp[0]
    }
}
