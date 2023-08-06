import argparse
from str_analysis.utils.canonical_repeat_unit import compute_canonical_motif


def parse_args():
    args = argparse.ArgumentParser()

    return args


def get_overlap(interval_tree, chrom, start_0based, end, canonical_motif):
    """Returns overlapping interval(s) from the interval tree, if any.

    Args:
        interval_tree (dict): a dictionary that maps chromosome names to IntervalTrees
        chrom (str): chromosome name
        start_0based (int): start position of the interval to check for overlap
        end (int): end position of the interval to check for overlap
        canonical_motif (str): the canonical motif to match

    Returns:
        list of strings: locus ids of entries in the IntervalTree that overlap the given interval chrom:start_0based-end
    """
    chrom = chrom.replace("chr", "")
    for locus_interval in interval_tree[chrom].overlap(start_0based, end):
        if locus_interval.data.canonical_repeat_unit != canonical_motif:
            continue
        matching_known_disease_associated_locus_id = locus_interval.data[1]
        return matching_known_disease_associated_locus_id

    return None


def main():
    args = parse_args()


if __name__ == "__main__":
    main()
