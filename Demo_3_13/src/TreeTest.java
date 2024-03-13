
class TreeNode {
    int value;
    TreeNode left;
    TreeNode right;

    TreeNode(int value) {
        this.value = value;
    }

    TreeNode(int value, TreeNode left, TreeNode right) {
        this.value = value;
        this.left = left;
        this.right = right;
    }
}

public class TreeTest {
    public String tree2str(TreeNode root) {
        StringBuilder str = new StringBuilder();
        treeNodestr(root, str);
        return str.toString();
    }

    public static void treeNodestr(TreeNode root, StringBuilder str) {
        if (root == null) {
            return;
        }
        str.append(root.value);
        if (root.left != null) {
            str.append("(");
            treeNodestr(root.left, str);
            str.append(")");
        } else {
            if (root.right != null) {
                str.append("()");
            } else {
                return;
            }
        }

        if (root.right != null) {
            str.append("(");
            treeNodestr(root.right, str);
            str.append(")");
        } else {
            return;
        }
    }

}
