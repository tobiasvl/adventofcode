use std::{
    fs::File,
    io::{self, BufRead},
    path::Path,
};

pub fn collect_lines<P>(filename: P) -> io::Result<Vec<String>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    io::BufReader::new(file).lines().collect()
}
