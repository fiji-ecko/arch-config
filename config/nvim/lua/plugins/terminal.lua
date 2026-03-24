return {
  {
    "akinsho/toggleterm.nvim",
    version = "*",
    keys = {
      { "<leader><CR>", "<cmd>ToggleTerm<CR>", desc = "Toggle terminal" },
      { "<leader>tf", "<cmd>ToggleTerm direction=float<CR>", desc = "Floating terminal" },
    },
    config = function()
      require("toggleterm").setup({
        size = 20,
        open_mapping = [[<c-\>]],
        direction = "horizontal",
      })
    end,
  }
}
