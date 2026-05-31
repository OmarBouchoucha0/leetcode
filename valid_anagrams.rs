use std::collections::HashMap;

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        if s.len() != t.len(){
            return false;
        }
        let mut seen: HashMap<char,i32> = HashMap::new();
        for c in s.chars(){
            seen.entry(c).and_modify(|count| *count += 1);
            seen.entry(c).or_insert(1);
        }
        for c in t.chars(){
            if seen.contains_key(&c){
                seen.entry(c).and_modify(|count| *count -= 1);
                if seen.get(&c) < Some(&0){
                    return false;
                }
            }else{
                return false;
            }
        }
        return true;
    }
}

