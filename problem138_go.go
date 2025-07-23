/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Next *Node
 *     Random *Node
 * }
 */

// 复制带随机指针的链表
// 复制带随机指针的链表
func copyRandomList(head *Node) *Node {
    // 如果原链表为空，直接返回nil
    if head == nil {
        return nil
    }
    
    // 第一步：在每个原节点后面创建一个新节点
    // 1->2->3 变成 1->1'->2->2'->3->3'
    for node := head; node != nil; node = node.Next.Next {
        // 创建新节点，值与原节点相同，Next指向原节点的下一个节点
        node.Next = &Node{Val: node.Val, Next: node.Next}
    }
    
    // 第二步：设置新节点的Random指针
    for node := head; node != nil; node = node.Next.Next {
        if node.Random != nil {
            // 新节点的Random指向原节点Random指向节点的下一个节点
            // 即原节点的Random的拷贝节点
            node.Next.Random = node.Random.Next
        }
    }
    
    // 第三步：分离两个链表
    headNew := head.Next // 新链表的头节点
    for node := head; node != nil; node = node.Next {
        nodeNew := node.Next // 当前新节点
        // 恢复原链表的Next指针
        node.Next = node.Next.Next
        // 设置新链表的Next指针
        if nodeNew.Next != nil {
            nodeNew.Next = nodeNew.Next.Next
        }
    }
    
    // 返回新链表的头节点
    return headNew
}

