Page({
  data:{
    num:0
  },
  handleInput(e){
    this.setData({
      num:e.detail.value
    });
  },
  handleTap(e){
    const operation=Number(e.currentTarget.dataset.operation);
    this.setData({
      num:Number(this.data.num)+operation
    });
  }
})