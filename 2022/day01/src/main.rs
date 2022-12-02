#![allow(clippy::unwrap_used)]

fn collect_elves(lines: &str) -> Vec<Vec<u32>> {
    lines
        .split("\n\n")
        .map(|elf| elf.lines().map(|x| x.parse().unwrap()).collect())
        .collect()
}

fn sum_elves(elves: &[Vec<u32>]) -> Vec<u32> {
    elves.iter().map(|elf| elf.iter().sum()).collect()
}

fn part1(lines: &str) -> u32 {
    *sum_elves(&collect_elves(lines)).iter().max().unwrap()
}

fn part2(lines: &str) -> u32 {
    let mut elves = sum_elves(&collect_elves(lines));
    elves.sort_unstable();
    elves.iter().sorted().rev().take(3).sum()
}

fn main() {
    let lines = std::fs::read_to_string(format!("{}/input", env!("CARGO_PKG_NAME"))).unwrap();
    println!("{}", part1(&lines));
    println!("{}", part2(&lines));
}

#[test]
#[allow(clippy::unwrap_used)]
fn day01() {
    let lines = std::fs::read_to_string("sample").unwrap();
    assert_eq!(part1(&lines), 24000);
    assert_eq!(part2(&lines), 45000);
}
