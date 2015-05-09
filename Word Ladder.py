"""
 Author:     Henry, henrylu518@gmail.com
 Date:       May 8, 2015
 Problem:    Word Ladder
 Difficulty: High
 Source:     http://leetcode.com/onlinejudge#question_127
 Notes:
 Given two words (start and end), and a dictionary, find the length of shortest transformation 
 sequence from start to end, such that:
 Only one letter can be changed at a time
 Each intermediate word must exist in the dictionary
 For example,
 Given:
 start = "hit"
 end = "cog"
 dict = ["hot","dot","dog","lot","log"]
 As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
 return its length 5.
 Note:
 Return 0 if there is no such transformation sequence.
 All words have the same length.
 All words contain only lowercase alphabetic characters.

 Solution: BFS.
"""

class Solution:
    # @param beginWord, a string
    # @param endWord, a string
    # @param wordDict, a set<string>
    # @return an integer
    def ladderLength(self, beginWord, endWord, wordDict):
        wordDict = set(wordDict) | set([endWord])
        def successor(word):
            successorWords = []
            for i in xrange(len(word)):
                for j in "abcdefghijklmnopqrstuvwxyz":
                    if word[i] != j:
                        newWord = word[:i] + j + word[i+1:]
                        if newWord in wordDict:
                            successorWords.append(newWord)
            return successorWords

        explored = set()
        queue = [(beginWord, 1)]
        while queue:
            word, steps = queue.pop(0)
            if word == endWord: 
                return steps
            if word not in explored:
                for w in successor(word):
                    if w not in explored:
                        queue.append((w, steps + 1))
                explored.add(word)
        return 0

