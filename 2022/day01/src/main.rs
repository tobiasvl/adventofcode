#![allow(clippy::unwrap_used)]

fn collect_elves(lines: &Vec<String>) -> Vec<Vec<usize>> {
    let mut elves = Vec::<Vec<usize>>::new();
    let mut elf = Vec::<usize>::new();

    for line in lines {
        if line.is_empty() {
            elves.push(elf);
            elf = Vec::<usize>::new();
        } else {
            elf.push(line.parse().unwrap());
        }
    }
    elves.push(elf);

    elves
}

fn part1(lines: &Vec<String>) -> usize {
    collect_elves(lines)
        .iter()
        .map(|elf| elf.iter().sum::<usize>())
        .max()
        .unwrap()
}

fn part2(lines: &Vec<String>) -> usize {
    let mut elves = collect_elves(lines)
        .iter()
        .map(|elf| elf.iter().sum::<usize>())
        .collect::<Vec<usize>>();

    elves.sort_unstable();

    elves.iter().rev().take(3).sum()
}

fn main() {
    let lines = util::collect_lines(format!("{}/input", env!("CARGO_PKG_NAME"))).unwrap();
    println!("{}", part1(&lines));
    println!("{}", part2(&lines));
}

#[test]
#[allow(clippy::unwrap_used)]
fn day01() {
    let lines = util::collect_lines("sample").unwrap();
    assert_eq!(part1(&lines), 24000);
    assert_eq!(part2(&lines), 45000);
}
