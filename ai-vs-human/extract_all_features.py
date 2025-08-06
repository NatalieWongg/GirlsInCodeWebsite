import tokenize
import os
import csv
import re
import keyword
from collections import Counter
import ast

def extract_lexical_features(file):
    
    with open(file, 'rb') as fin:  
        tokens_list = list(tokenize.tokenize(fin.readline))
        meaningful_tokens = [tokval for toknum, tokval, *_ in tokens_list if toknum not in (tokenize.ENCODING, tokenize.ENDMARKER, tokenize.STRING, tokenize.NUMBER)]
        num_comments = sum(1 for tok in tokens_list if tok.type == tokenize.COMMENT)
        num_lines = sum(1 for tok in tokens_list if tok.type == tokenize.NL or tok.type == tokenize.NEWLINE)
        comment_density = num_comments / num_lines
        avg_token_length = sum(len(token) for token in meaningful_tokens) / len(meaningful_tokens) if meaningful_tokens else 0
        identifiers = [tok.string for tok in tokens_list if tok.type == tokenize.NAME]
        num_identifiers = len(identifiers)
        avg_identifier_length = sum(len(name) for name in identifiers) / num_identifiers if num_identifiers else 0
        snake_case = len({name for name in identifiers if '_' in name and len(name) > 1})
        

    return {
        'avg_token_length': round(avg_token_length,2),
        'avg_identifier_length': round(avg_identifier_length,2),
        'num_lines': num_lines,
        'num_tokens': len(tokens_list),
        'snake_case_count': snake_case,
        'comment_density': round(comment_density,2),
    }




def extract_structural_features(file):
    with open(file, "r", encoding="utf-8") as fin:
        lines = fin.readlines()  
        num_lines = len(lines)
        avg_line_length = sum(len(line.strip()) for line in lines) / num_lines if num_lines > 0 else 0
        blank = sum(1 for line in lines if line.strip() == "")
        docstrings = sum(1 for line in lines if line.strip().startswith('"""'))
        comment_lines = sum(1 for line in lines if line.strip().startswith("#"))
        tabs = sum(1 for line in lines if line.startswith("  ") or line.startswith("\t"))
        eq_spaces = sum(1 for line in lines if " = " in line) + sum(1 for line in lines if ", " in line)
        total_eq = sum(1 for line in lines if "=" in line) + sum(1 for line in lines if "," in line)
        space_ratio = eq_spaces/total_eq if total_eq else 0
        
        return {
            "avg_line_length": round(avg_line_length,1),
            "tabs": tabs,
            "blank_lines": blank,
            "docstrings": docstrings,
        }

class ASTFeatureExtractor(ast.NodeVisitor):
    def __init__(self):
        self.function = False
        self.for_loop_count = 0
        self.while_loop_count = 0
        self.max_depth = 0
        self.total_loop_count = 0
        self.assignments_count = 0
        self.list_comprehension_count = 0
        self.for_loops_with_append = 0
        self.else_in_loop = 0

    def visit_FunctionDef(self, node):
        self.function = True
        

    def visit_For(self, node):
        self.for_loop_count += 1
        self.total_loop_count += 1
        for child in ast.walk(node):
            if isinstance(child, ast.Call) and isinstance(child.func, ast.Attribute):
                if child.func.attr == "append":
                    self.for_loops_with_append += 1
            
        if node.orelse:
            self.else_in_loop += 1
        self.generic_visit(node)


    def visit_While(self, node):
        self.while_loop_count += 1
        self.total_loop_count += 1
        self.generic_visit(node)
    
    def visit_Assign(self, node):
        self.assignments_count +=1
        self.generic_visit(node)

    def get_max_depth(self, node, depth=0):
        if not isinstance(node, ast.AST):
            return depth
        return max([self.get_max_depth(child, depth + 1) for child in ast.iter_child_nodes(node)] + [depth])
    
    def visit_ListComp(self, node):
            self.list_comprehension_count += 1
            self.generic_visit(node)



def extract_ast_features(file):
    with open(file, "r", encoding="utf-8") as fin:
        code = fin.read() 
        try:
            tree = ast.parse(code)
            extractor = ASTFeatureExtractor()
            extractor.visit(tree)
            depth = extractor.get_max_depth(tree)
            return {
                "function": extractor.function,
                "for_loop_count": extractor.for_loop_count, 
                "while_loop_count": extractor.while_loop_count,
                "total_loop_count": extractor.total_loop_count,
                "ast_depth": depth,
                "assignment_count": extractor.assignments_count,
                "list_comprehension_count": extractor.list_comprehension_count,
                "for_loops_with_append": extractor.for_loops_with_append,
                "else_in_loop": extractor.else_in_loop,
            }
        except Exception as e:
            return {"error": str(e)}

def extract_all_features(file):
    features = {}
    features.update(extract_lexical_features(file))
    features.update(extract_structural_features(file))
    features.update(extract_ast_features(file))
    return features

fout = 'features.csv'
data = []

for folder, label in [('human_samples', 'human'), ('ai_samples', 'ai')]:
    for filename in os.listdir(folder):
        if filename.endswith('.py'):
            full_path = os.path.join(folder, filename)
            features={}
            features["filename"] = filename
            features.update(extract_all_features(full_path))
            features["label"] = label
            data.append(features)


with open(fout, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)

import pandas as pd

# Load the CSV file
df = pd.read_csv('features.csv')

# Sort by the 'filename' column
df_sorted = df.sort_values(by='filename')

# Save the reordered CSV to a new file (or overwrite the original)
df_sorted.to_csv('sorted_file.csv', index=False)

