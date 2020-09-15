using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;
using Shamped.Data.Entities;

namespace Shamped.Data.Configurations
{
    public class PostConfiguration : IEntityTypeConfiguration<PostEntity>
    {
        public void Configure(EntityTypeBuilder<PostEntity> builder)
        {
            builder.Property(e => e.PostId).ValueGeneratedNever();
            builder.Property(e => e.CommentEnabled);
            builder.Property(e => e.ContentAbstract).HasMaxLength(1024);

            builder.Property(e => e.CreateAt);
            builder.Property(e => e.Content);

            builder.Property(e => e.Slug).HasMaxLength(128);
            builder.Property(e => e.Title).HasMaxLength(128);
        }
    }
}
