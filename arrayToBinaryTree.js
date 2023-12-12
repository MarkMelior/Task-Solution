function TreeNode(val, left, right) {
	this.val = val === undefined ? 0 : val
	this.left = left === undefined ? null : left
	this.right = right === undefined ? null : right
}

exports.arrayToBinaryTree = function arrayToBinaryTree(rootArray, index = 0) {
	if (index >= rootArray.length || rootArray[index] === null) {
		return null
	}

	const currentNode = new TreeNode(rootArray[index])
	const leftIndex = 2 * index + 1
	const rightIndex = 2 * index + 2

	currentNode.left = arrayToBinaryTree(rootArray, leftIndex)
	currentNode.right = arrayToBinaryTree(rootArray, rightIndex)

	return currentNode
}
