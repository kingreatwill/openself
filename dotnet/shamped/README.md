		public Guid Id { get; set; } # 主键
		public string UniqueId { get; set; } # 加密ID
        public string Title { get; set; } # 标题
		public string Slug { get; set; } # 静态链接
		public string Author { get; set; } # 作者 
		public string ContentAbstract { get; set; } # 摘要
        public string Content { get; set; } # 内容
		public DateTime CreateOnUtc { get; set; }# 创建日期
		
        public bool CommentEnabled { get; set; } # 是否开启评论 
        public bool IsPublished { get; set; } # 是否发布
        public bool IsToSiteMap { get; set; } # 是否 包含到SiteMap
        public bool IsFeedIncluded { get; set; } # 是否添加RSS
        public string LanguageCode { get; set; } # 语言
		
        public Tag[] Tags { get; set; } # 标签
        public Category[] Categories { get; set; } # 分类
		
        public DateTime? PubDateUtc { get; set; } # 发布日期
        public DateTime LastModifiedUtc { get; set; } = DateTime.UtcNow; # 最后更新日期
		
		 // not currently used but could be later
        public string ImageUrl { get; set; } # 图片
        public string ThumbnailUrl { get; set; } #  图片略图
		public bool IsDeleted
		public int Revision #修订
		
		PostgreSQL版本13
Comment
Category
Tag		
https://github.com/EdiWang/Moonglade/blob/master/src/Moonglade.Setup/Data/init-sampledata.sql
https://github.com/EdiWang/Moonglade/blob/master/src/Moonglade.Setup/Data/schema-mssql-140.sql

CREATE TABLE [Post](
[Id] [uniqueidentifier] PRIMARY KEY NOT NULL,
[Title] [nvarchar](128) NULL,
[Slug] [nvarchar](128) NULL,
[PostContent] [nvarchar](max) NULL,
[CommentEnabled] [bit] NOT NULL,
[CreateOnUtc] [datetime] NOT NULL,
[ContentAbstract] [nvarchar](1024) NULL) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]


CREATE TABLE [PostExtension](
[PostId] [uniqueidentifier] PRIMARY KEY NOT NULL,
[Hits] [int] NOT NULL,
[Likes] [int] NOT NULL)


CREATE TABLE [PostPublish](
[PostId] [uniqueidentifier] PRIMARY KEY NOT NULL,
[IsPublished] [bit] NOT NULL,
[ExposedToSiteMap] [bit] NOT NULL,
[IsFeedIncluded] [bit] NOT NULL,
[LastModifiedUtc] [datetime] NULL,
[IsDeleted] [bit] NOT NULL,
[PubDateUtc] [datetime] NULL,
[Revision] [int] NULL,
[ContentLanguageCode] [nvarchar](8) NULL)