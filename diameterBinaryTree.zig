const std = @import("std");

const TreeNode = struct {
    val: i32,
    left: ?*TreeNode,
    right: ?*TreeNode,
};
fn diameterOfBinaryTree(root: ?*TreeNode) u32 {
    if (root == null) {
        return 0;
    }
    if (root.?.left == null and root.?.right == null) {
        return 1;
    }
    const max_left: u32 = 0;
    const curr_left: u32 = 0;
    var curr_node = root.?;
    while (curr_node.left != null and curr_node.right != null) {
        if (curr_node.left == null) {
            curr_node = curr_node.right.?;
            curr_left -= 1;
        } else {
            curr_node = curr_node.left.?;
            curr_left += 1;
            if (curr_left > max_left) {
                max_left = curr_left;
            }
        }
    }
    const max_right: u32 = 0;
    const curr_right: u32 = 0;
    curr_node = root.?;
    while (curr_node.left != null and curr_node.right != null) {
        if (curr_node.right == null) {
            curr_node = curr_node.left.?;
            curr_right -= 1;
        } else {
            curr_node = curr_node.right.?;
            curr_left += 1;
            if (curr_right > max_right) {
                max_right = curr_right;
            }
        }
    }
    const res = max_left + max_right;
    return res;
}

pub fn main() void {
    std.debug.print("hello", .{});
}

test "1" {}
