#![allow(clippy::unwrap_used)]
use itertools::Itertools;
use std::str::FromStr;

#[derive(PartialEq, Clone, Copy)]
enum Rps {
    Rock = 1,
    Paper = 2,
    Scissors = 3,
}

impl FromStr for Rps {
    type Err = ();
    fn from_str(play: &str) -> Result<Rps, ()> {
        Ok(match play {
            "A" | "X" => Rps::Rock,
            "B" | "Y" => Rps::Paper,
            "C" | "Z" => Rps::Scissors,
            _ => unreachable!(),
        })
    }
}

fn win(play: Rps) -> Rps {
    match play {
        Rps::Rock => Rps::Scissors,
        Rps::Scissors => Rps::Paper,
        Rps::Paper => Rps::Rock,
    }
}

fn lose(play: Rps) -> Rps {
    match play {
        Rps::Rock => Rps::Paper,
        Rps::Scissors => Rps::Rock,
        Rps::Paper => Rps::Scissors,
    }
}

fn play(play: Rps, outcome: &str) -> Rps {
    match outcome {
        "X" => win(play),
        "Y" => play,
        "Z" => lose(play),
        _ => unreachable!(),
    }
}

fn score(rounds: Vec<(Rps, Rps)>) -> u32 {
    let mut score = 0;
    for (opponent, reply) in rounds {
        score += reply as u32;

        score += if win(reply) == opponent {
            6
        } else if reply == opponent {
            3
        } else {
            0
        };
    }

    score
}

fn part1(input: &str) -> u32 {
    let rounds = input
        .lines()
        .map(|line| {
            line.split(' ')
                .map(|play| Rps::from_str(play).unwrap())
                .next_tuple()
                .unwrap()
        })
        .collect::<Vec<(Rps, Rps)>>();

    score(rounds)
}

fn part2(input: &str) -> u32 {
    let rounds = input
        .lines()
        .map(|line| line.split(' ').next_tuple().unwrap())
        .map(|(opponent, outcome)| {
            (
                Rps::from_str(opponent).unwrap(),
                play(Rps::from_str(opponent).unwrap(), outcome),
            )
        })
        .collect::<Vec<(Rps, Rps)>>();

    score(rounds)
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
    assert_eq!(part1(&input), 15);
}

#[test]
#[allow(clippy::unwrap_used)]
fn test_part2() {
    let input = std::fs::read_to_string("sample").unwrap();
    assert_eq!(part2(&input), 12);
}
