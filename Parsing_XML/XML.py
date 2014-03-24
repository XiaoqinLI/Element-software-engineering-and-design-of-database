#!/usr/bin/env python3

"""
#------------------------------
# projects/Search in XML/XML.py
author: Roberto Salinas, Xiaoqin LI
#------------------------------
"""
import sys
from xml.etree.ElementTree import Element, fromstring, iselement



def xmlRead(stdin):
    """
    stdin: system input stream
    return a string read from a xml data
    """
    
    xml_str_data = "<xml>" + "".join(stdin.read()) + "</xml>"
    assert(type(xml_str_data) is str)
    return xml_str_data

def xmlPrint (w, output_list) :
    """
    prints the values of output_list
    w is a writer
    """
    
    for entry in output_list:
        w.write(str(entry) + "\n")
    w.write("\n")
    
def xmlSolve(stdin, stdout):
    """
    stdin: system input stream
    stout: system output stream
    root is the whole single root element tree
    root_list: all child element
    """
    
    root =  fromstring(xmlRead(stdin))
    assert(type(root) is Element)
    root_list = (root.findall("*"))
    assert(type(root_list) is list)
    
    for x in range(0,len(root_list),2):   
        result_list = xmleval(root_list[x], root_list[x+1])
        xmlPrint(stdout, result_list)       
    
def xmleval(source_tree, target_tree):
    """
    Searches for the target_tree in the XML source tree
    Returns the number of occurance and location of each occurrence.
    target_string: the string of query element tree
    goal_list: a list of target_tree found in source tree.
    output_list is the list of output:
    first element in the list denotes the number of occurance
    other elements denote the location(id) of each occurance
    source_tree2 : created by inserting source tree in an empty element tree.
                   the reason to do so is to include the top layer of source tree in the searching.
    Using element.set() and element.get() to set and get attribute key on the element to value,
                   which reduce algorithm complexity compared to previous nested searching for loop
    """
  
    Ocurrence_counter = 0
    output_list = []
    output_list.append(Ocurrence_counter)
    
    Start_String = ".//"    # Selects all subelements on all level beneath the current element
    target_string = get_Target_String(target_tree,Start_String)
    

    tag_list = source_tree.iter()
    for (location,tag) in enumerate (tag_list,1):
        tag.set('#', str(location))
    
    '''
    # --------------previous indexing methods, retired------------------    
    index_tag = 1
    index_list = []
    for entry in tag_list:
        index_list.append([index_tag, entry])        
        index_tag += 1
    # ------------------------------------------------------------------
    '''
    source_tree2 = Element("")
    source_tree2.insert(0,source_tree)
    assert(iselement(source_tree2) == True)
    goal_list = (source_tree2.findall(target_string))   
    assert(type(goal_list) is list)
    
    for entry in goal_list:
        output_list.append(int(entry.get('#')))
        Ocurrence_counter +=1
    '''       
    # --------------previous indexing methods, retired------------------       
    for x in goal_list:
        for y in index_list:
            if x == y[1]:
                assert(type(y[0] is int))
                output_list.append(y[0])
                Ocurrence_counter +=1
    # ------------------------------------------------------------------
    '''          
    output_list[0] = Ocurrence_counter   
    assert(type(output_list) is list)
    return output_list 
   
def get_Target_String(target_tree,Start_String):
    '''
    create and return the query string from target tree by recursion method
    it returns a string that is gonna be used at the argument of element.findall() to search target tree.
    '''
      
    Start_String += target_tree.tag  
   
    for entry in target_tree:
        Start_String += "/"       
        Start_String = get_Target_String(entry,Start_String)
        Start_String += "/.."       # Select the parent element
    
    return Start_String


