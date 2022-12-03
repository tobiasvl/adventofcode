#![allow(clippy::unwrap_used)]
use std::collections::HashSet;

use itertools::Itertools;

fn chars_to_priority(lines: &mut dyn Iterator<Item = char>) -> u32 {
    lines
        .map(|c| {
            if c.is_lowercase() {
                c as u32 - 96
            } else {
                c as u32 - 64 + 26
            }
        })
        .sum::<u32>() as u32
}

fn part1(input: &str) -> u32 {
    let mut lines =
        input
            .lines()
            .map(|line| line.split_at(line.len() / 2))
            .map(|(comp1, comp2)| {
                comp1
                    .chars()
                    .collect::<HashSet<char>>()
                    .intersection(&comp2.chars().collect::<HashSet<char>>())
                    .copied()
                    .next()
                    .unwrap()
            });

    chars_to_priority(&mut lines)
}

fn part2(input: &str) -> u32 {
    let groups = input.lines().chunks(3);
    let mut lines = groups
        .into_iter()
        .map(|mut group| group.next_tuple::<(&str, &str, &str)>().unwrap())
        .map(|(sack1, sack2, sack3): (&str, &str, &str)| {
            sack1
                .chars()
                .collect::<HashSet<char>>()
                .intersection(&sack2.chars().collect::<HashSet<_>>())
                .copied()
                .collect::<HashSet<char>>()
                .intersection(&sack3.chars().collect::<HashSet<_>>())
                .copied()
                .next()
                .unwrap()
        });

    chars_to_priority(&mut lines)
}

fn main() {
    let input = std::fs::read_to_string(format!("{}/input", env!("CARGO_PKG_NAME"))).unwrap();
    println!("{}", part1(&input));
    println!("{}", part2(&input));
}

#[test]
#[allow(clippy::unwrap_used)]
fn test_part1() {
    let input = std::fs::read_to_string("sample").unwrap();
    assert_eq!(part1(&input), 157);
}

#[test]
#[allow(clippy::unwrap_used)]
fn test_part2() {
    let input = std::fs::read_to_string("sample").unwrap();
    assert_eq!(part2(&input), 70);
}
