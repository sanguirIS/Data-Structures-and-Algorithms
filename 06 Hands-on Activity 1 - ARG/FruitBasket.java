mport javax.swing.*;
import javax.swing.tree.*;

public class HtmlTree {
    public static void main(String[] args) {
        // Create tree nodes
        DefaultMutableTreeNode root = new DefaultMutableTreeNode("html");
        DefaultMutableTreeNode head = new DefaultMutableTreeNode("head");
        DefaultMutableTreeNode title = new DefaultMutableTreeNode("title");
        DefaultMutableTreeNode body = new DefaultMutableTreeNode("body");
        DefaultMutableTreeNode h1 = new DefaultMutableTreeNode("h1");
        DefaultMutableTreeNode p = new DefaultMutableTreeNode("p");

        // Build tree structure
        root.add(head);
        root.add(body);
        head.add(title);
        body.add(h1);
        body.add(p);

        // Create JTree
        JTree tree = new JTree(root);

        // Display JTree in a frame
        JFrame frame = new JFrame("Html Tree");
        frame.add(new JScrollPane(tree));
        frame.setSize(400, 300);
        frame.setVisible(true);
    }
}